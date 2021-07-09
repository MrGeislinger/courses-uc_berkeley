import requests
from bs4 import BeautifulSoup


# TODO: Read course page to get to topic pages
# TODO: Get courses from topic page

# Read in course
def get_course_info(course_block_soup):
    data = {}
    # Get basic course info like title, code, etc.
    basic_course_info = course_block_soup.find(class_='courseblocktitle')
    data['code'] = basic_course_info.find(class_='code').text
    data['title'] = basic_course_info.find(class_='title').text
    data['units'] = basic_course_info.find(class_='hours').text

    # Get all spans that are part
    course_desc = course_block_soup.find(class_='courseblockdesc')
    # TODO: Document what class multiple spans are from
    data['description'] = '\n'.join(
                                child.text 
                                for child 
                                in course_desc.findChildren('span', recursive=False))
   
    return data



topic_url = 'http://guide.berkeley.edu/courses/aerospc/'
response = requests.get(topic_url)
soup = BeautifulSoup(response.text, 'html.parser')

course_blocks = soup.find_all(class_='courseblock')
info = get_course_info(course_blocks[0])
print(info)