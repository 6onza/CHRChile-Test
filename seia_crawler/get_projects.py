from bs4 import BeautifulSoup
import requests
import json
import re

# user agent to avoid 403 error
AGENT = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def get_projects_info(project_page_n, cookie):
    # this function gets the project info from the rows of the table in the page

    projects = [] 
    # the url is the same but the page number changes
    url: str ='https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php' + '?_paginador_refresh=1&_paginador_fila_actual=' + str(project_page_n)
    try:
        request = requests.get(url, headers=AGENT, cookies={'PHPSESSID': cookie})
        request.raise_for_status()
        
        soup = BeautifulSoup(request.content, 'html.parser')

        # get the rows of the table where the project info is
        table = soup.find('table', {'class': 'tabla_datos'})
        t_body = table.find('tbody')
        rows = t_body.find_all('tr')

        if rows:
            for row in rows:
                cols = row.find_all('td')
                # clean map link
                mapa = cols[9].find('a').get('onclick') if cols[9].find('a') else None
                mapa = mapa.replace("window.open('", '').replace("', 'mapa')", '') if mapa else None
                mapa = 'https://seia.sea.gob.cl' + mapa if mapa else None

                project = {
                    'number': cols[0].text,
                    'name': cols[1].text,
                    'type': cols[2].text,
                    'region': cols[3].text,
                    'typology': cols[4].text,
                    'owner': cols[5].text,
                    'investment': cols[6].text,
                    'date': cols[7].text,
                    'status': cols[8].text,
                    'map': mapa
                }
                projects.append(project)
        else:
            print('No projects found')

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    
    except requests.exceptions.RequestException as err:
        print(f'Other error occurred: {err}')
    
    finally:
        return projects

def get_total_pages_and_cookie():
    total_pages = 0
    cookie = ''
    try:
        url = 'https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php'
        request = requests.get(url, headers=AGENT)
        request.raise_for_status()

        # get the cookie to use in the next request
        cookie = request.cookies.get('PHPSESSID')

        soup = BeautifulSoup(request.content, 'html.parser')
        
        # get the total number of pages
        info_resultado = soup.find('div', {'id': 'info_resultado'})

        if info_resultado:
            pages_text = info_resultado.find(text=re.compile(r'Número de páginas'))
            if pages_text:
                total_pages = int(pages_text.split(':')[-1].replace(',', '').strip()) 

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')

    except requests.exceptions.RequestException as err:
        print(f'Other error occurred: {err}')

    return total_pages, cookie


def get_projects():
    total_pages, cookie = get_total_pages_and_cookie()
    projects: list = []

    for page in range(1, total_pages + 1):
        project = get_projects_info(page, cookie)
        if project:
            projects.append(project)

    return projects


def save_projects_to_json():
    # this function gets all the projects and saves them to a json file
    # it won't save the projects till the end

    total_pages, cookie = get_total_pages_and_cookie() 
    # if you want to get a specific number of pages specify below:
    # total_pages = 3

    # list to store the projects
    projects: list = []

    try:
        for page in range(1, total_pages + 1):
            print(f'Getting projects from page {page} of {total_pages}')
            project = get_projects_info(page, cookie)
            if project:
                projects.extend(project)
        
        # write the projects to a json file
        with open('projects.json', 'w') as f:
            json.dump(projects, f, indent=4)

    except Exception as err:
        print(f'An error occurred: {err}')


if __name__ == '__main__':
    save_projects_to_json()
