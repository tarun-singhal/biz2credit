import django_tables2 as tables
import requests
from requests.auth import HTTPBasicAuth
from django_tables2.utils import A  # alias for Accessor


response = requests.get('http://localhost:5000/api/v1/story', auth=HTTPBasicAuth('admin', 'SuperSecretPwd'))
data = response.json()
class BlogTable(tables.Table):
    title = tables.Column()
    content = tables.Column()
    name = tables.Column()
    vote_up = tables.LinkColumn('blog_list', text='Up', orderable=False) 
    vote_down = tables.LinkColumn('blog_list', text='Down',  orderable=False)
    _id = tables.Column("ID")
    action = tables.LinkColumn('blog_list', text="Edit", orderable=False)

    class Meta:
        sequence = ('vote_up', 'vote_down', '_id',  'title', 'name', 'content', 'action')
        template_name = 'django_tables2/bootstrap4.html'
        orderable = True

    def render_row_number(self):
        return 'Row %d' % next(self.counter)

table = BlogTable(data['resp'])  




