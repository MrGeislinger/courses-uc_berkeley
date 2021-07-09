import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime


# TODO: Read course page to get to topic pages
def get_topics(homepage_url):  
    response = requests.get(homepage_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find all the "letter" sections to find the unordered list of topics
    topic_headings = soup.find_all(class_='letternav-head')
    topics = []
    for topic_heading in topic_headings:
        topics.extend(
                (li.a.text, li.a.get('href')) 
                    for li 
                    in topic_heading.find_next_sibling('ul').findChildren('li')
        )
    
    return topics

# Get courses from topic page
def get_courses_from_topic_page(topic_url):
    response = requests.get(topic_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    course_blocks = soup.find_all(class_='courseblock')
    return course_blocks

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
                                    in course_desc.findChildren(
                                                            'span', 
                                                            recursive=False))
   
    return data


### Main Usage
base_url = 'http://guide.berkeley.edu'
topic_urls = get_topics('http://guide.berkeley.edu/courses/')

for topic_name, topic_url_rel in topic_urls:
    # Use
    topic_name_inferred = topic_url_rel.split('/')[-2]
    print(datetime.datetime.now(), topic_name)
    
    topic_url = f'{base_url}{topic_url_rel}'
    course_blocks = get_courses_from_topic_page(topic_url=topic_url)

    # Iterate over each course and create a DataFrame
    df = pd.DataFrame(data=(get_course_info(course_block) for course_block in course_blocks))
    df['topic'] = topic_name

    # DEBUG: show the data makes sense
    df.to_csv(f'{topic_name}.csv', index=False)