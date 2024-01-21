import itertools
from bs4 import BeautifulSoup

def get_reserable_xpath(contents: str, time: list[str], eager: bool) -> list[str]:
  """
  予約可能なXPathを取得する
  :param contents: HTML
  :param time: 予約したい時間帯の開始時刻
  :param eager: 指名不可な時間帯も含めるか
  :return: 予約可能なXPathのリスト
  """

  soup = BeautifulSoup(contents, 'html.parser')
  time_slots = []
  i = 1 # 当日分は検索対象から外す

  while True:
    input_tag = soup.find('input', {'id': f'lst_ih_{i}'})
    if not input_tag:
      break

    div_tag = input_tag.find_next_sibling('div')
    if not div_tag:
      i += 1
      continue

    date_tag = div_tag.find('span', {'class': ['lbl', 'sun', 'sat']})
    if not date_tag:
      i += 1
      continue
    
    # 日付の一覧を表示
    # print(date_tag.text.strip())

    badge = div_tag.find('span', {'class': ['badge', 'badge badge_pink']})
    if not badge or badge.text.strip() != "空":
      i += 1
      continue

    date_div = div_tag.find_next_sibling('div')
    time_info = date_div.find_all('div', {'class': 'blocks'})

    print(f"date: {date_tag.text.strip()}")
    
    if time_info:
      for e in time_info:
        time_range = e.find_all('span', {'class': 'lbl'})
        start_time = time_range[2].text
        end_time = time_range[4].text
        status = time_range[5].text.strip()
        e_selection = e.parent

        print(f"  time: {start_time} ~ {end_time}, status: {status}")
        
        time_slots.append((start_time, status, xpath_soup(e_selection)))
    i += 1

  # Filter the time slots based on the desired time and status
  results = [xpath for start_time, status, xpath in time_slots if start_time in time and (status == "指名　○" or (status == "指名　×" and eager))]

  return results

def xpath_soup(element):
  """
  Generate xpath of soup element
  :param element: bs4 text or node
  :return: xpath as string
  """
  components = []
  child = element if element.name else element.parent
  for parent in child.parents:
    """
    @type parent: bs4.element.Tag
    """
    previous = itertools.islice(parent.children, 0, parent.contents.index(child))
    xpath_tag = child.name
    xpath_index = sum(1 for i in previous if i.name == xpath_tag) + 1
    components.append(xpath_tag if xpath_index == 1 else '%s[%d]' % (xpath_tag, xpath_index))
    child = parent
  components.reverse()
  return '/%s' % '/'.join(components)


if __name__ == '__main__':
  conditions = ["09:00", "12:00"]

  with open('res/reserve.html', 'r', encoding='utf-8') as f:
    contents = f.read()
    print(get_reserable_xpath(contents, conditions, False))
