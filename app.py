import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".s-post-summary") # class in html code
print(questions[0].attrs)
print(questions[0].get("id", 0))
question_link = questions[0].select_one(".s-link")
print(question_link)
question_text = question_link.getText()
print(question_text)

for question in questions:
    question_link_1 = question.select_one(".s-link")
    # print(question_link_1)
    question_text_1 = question_link_1.getText()
    print(question_text_1)
    print('Votes:', question.select_one(".s-post-summary--stats-item-number").getText())
