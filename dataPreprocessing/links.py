import pandas as pd
import re

def extract_links(data):
    # قائمة لتخزين الروابط وأرقام الوثائق المرتبطة بها
    links = []
    doc_ids = []

    # التعبير العادي لاستخراج الروابط
    link_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    # الحصول على رقم الوثيقة والروابط لكل صف في البيانات
    for index, row in data.iterrows():
        doc_id = row['doc_id']
        text = row['doc']
        
        # البحث عن الروابط في النص
        found_links = re.findall(link_pattern, text)
        for link in found_links:
            if link.strip() != '':
                # إضافة الروابط وأرقام الوثائق إلى القوائم
                links.append(link)
                doc_ids.append(doc_id)

        # إضافة الروابط وأرقام الوثائق إلى القوائم
        # links.extend(found_links)
        # doc_ids.extend([doc_id] * len(found_links))

    # إنشاء إطار البيانات لتخزين الروابط وأرقام الوثائق
    df = pd.DataFrame({'doc_id': doc_ids, 'link': links})
    
    return df