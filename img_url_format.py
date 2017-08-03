
import pandas as pd
import xlsxwriter

xl = pd.ExcelFile('img.xlsx')

# output xl writer
writer = pd.ExcelWriter('new_img_url.xlsx', engine='xlsxwriter')

# read respective sheets of excel file
df1 = xl.parse('SimpleVisible')
df2 = xl.parse('ParentSKuList')

# define new base url to reformat
new_base_url = 'http://www.religiousgiftwarehouse.com/media/catalog/product/'


# function for apply calls
def url_reformat(vals):
    '''
        - vals: the old image url
        - separate file name from old url and change its type to str to use lower(), coz sometimes it can only contain numbers
        - take first two chars from img name, change it to str and join it by '/', representing the directory structure
        - join above two with the new base url
    '''
    return new_base_url + '/' .join(str(vals).split('/')[-1][:2].lower()) + '/' + str(vals).split('/')[-1].lower()


# reformat for df1, create new column in first sheet
df1['new_img_url'] = df1['image_url'].apply(url_reformat)

# reformat for df2, create new column in second sheet
df2['new_img_url'] = df2['Image_url'].apply(url_reformat)


# write output to new file
df1.to_excel(writer, sheet_name='SimpleVisible', index=False)
df2.to_excel(writer, sheet_name='ParentSKuList', index=False)
writer.save()
