
class TestUrls():

    def test_add_employee_url(self, urls):
        # test register employee url
        path = urls['add_employee']
        assert path == '/api/v1/auth/add/'

    def test_employee_role_url(self, urls):
        # test add role url
        path = urls['employee_role_url']
        assert path == '/api/v1/auth/addrole/'

    def test_login_url(self, urls):
        # test login url
        path = urls['login_url']
        assert path == '/api/v1/auth/login/'

    def test_expense_category_url(self, urls):
        # test expense category url
        path = urls['expense_category_url']
        assert path == '/api/v1/requests/category/'

    def test_staffs_url(self, urls):
        # test expense request url
        path = urls['staffs_url']
        assert path == '/api/v1/requests/staffs/'

    def test_allstaffs_url(self, urls):
        # test all expense request url
        path = urls['allstaffs_url']
        assert path == '/api/v1/requests/allstaffs/'

    def test_approve_request_url(self, urls):
        # test approve expense requests url
        path = urls['approve_request_url']
        assert path == '/api/v1/requests/approve/1'
