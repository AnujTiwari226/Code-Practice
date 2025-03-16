import pandas as pd


class Solution:
    def big_countries(self):
        data = {
            'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
            'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
            'area': [652230, 28748, 2381741, 468, 1246700],
            'population': [25500100, 2831741, 37100000, 78115, 20609294],
            'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
        }
        world = pd.DataFrame(data)
        cols = ['name', 'area', 'population']
        df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)][cols]
        print(df)

    def find_customers(self) -> pd.DataFrame:
        customers_data = {
            'id': [1, 2, 3, 4],
            'name': ['Joe', 'Henry', 'Sam', 'Max']
        }
        orders_data = {
            'id': [1, 2],
            'customerId': [3, 1]
        }
        customers_df = pd.DataFrame(customers_data)
        orders_df = pd.DataFrame(orders_data)
        orders_df.rename(columns={'id': 'order_id'}, inplace=True)
        merged_df = pd.merge(
            left=customers_df,
            left_on = 'id',
            right=orders_df,
            right_on='customerId',
            how='left'
        )
        df= merged_df[merged_df['order_id'].isna()]
        print(df[['name']])

    def find_customersII(self):
        customers_data = {
            'id': [1, 2, 3, 4],
            'name': ['Joe', 'Henry', 'Sam', 'Max']
        }
        orders_data = {
            'id': [1, 2],
            'customerId': [3, 1]
        }
        customers_df = pd.DataFrame(customers_data)
        orders_df = pd.DataFrame(orders_data)

        df = customers_df[~customers_df['id'].isin(orders_df['customerId'])]
        print(df[['name']].rename(columns={'name': 'Customers'}))

    def article_views(self) -> pd.DataFrame:
        article_views_data = {
            'article_id': [1, 1, 2, 2, 4, 3, 3],
            'author_id': [3, 3, 7, 7, 7, 4, 4],
            'viewer_id': [5, 6, 7, 6, 1, 4, 3],
            'view_date': ['2019-08-01', '2019-08-02', '2019-08-01', '2019-08-02', '2019-07-22', '2019-07-21',
                          '2019-07-21']
        }
        views = pd.DataFrame(article_views_data)
        # Count unique viewers per (author_id, article_id) group
        views['unique_viewers'] = views.groupby(['author_id', 'article_id'])['viewer_id'].transform('nunique')

        df = views[(views['author_id'] == views['viewer_id']) & (views['unique_viewers'] > 0)]

        # Drop duplicates by author_id to get unique authors
        authors = df.drop_duplicates(subset=['author_id'])[['author_id']].sort_values(by='author_id',ascending=True)

        print(authors)

    def invalid_tweets(self) -> pd.DataFrame:
        data = [
            {"tweet_id": 1, "content": "Vote for Biden"},
            {"tweet_id": 2, "content": "Let us make America great again!"}
        ]
        df = pd.DataFrame(data)
        df['length'] = df['content'].apply(lambda x: len(x))
        print(df[df['length'] > 15][['tweet_id']])

    def calculate_special_bonus(self) -> pd.DataFrame:
        data = [
            {"employee_id": 2, "name": "Meir", "salary": 3000},
            {"employee_id": 3, "name": "Michael", "salary": 3800},
            {"employee_id": 7, "name": "Addilyn", "salary": 7400},
            {"employee_id": 8, "name": "Juan", "salary": 6100},
            {"employee_id": 9, "name": "Kannon", "salary": 7700}
        ]

        employees = pd.DataFrame(data)
        # employees['even_odd'] = employees[employees['employee_id'].apply(lambda x: True if x % 2 == 0 else False)]
        mask1 = employees['employee_id'].apply(lambda x: True if x % 2 == 0 else False)
        mask2 = employees['name'].apply(lambda x : True if x[0] == 'M' else False)
        mask = mask1 | mask2
        employees['bonus'] = employees.loc[~mask, 'salary'].fillna(0)
        employees['bonus'].fillna(0, inplace=True)
        print(employees[['bonus']].astype('int32'))

    def valid_emails(self) -> pd.DataFrame:
        data = [
            {"user_id": 1, "name": "Winston", "mail": "winston@leetcode.com"},
            {"user_id": 2, "name": "Jonathan", "mail": "jonathanisgreat"},
            {"user_id": 3, "name": "Annabelle", "mail": "bella-@leetcode.com"},
            {"user_id": 4, "name": "Sally", "mail": "sally.come@leetcode.com"},
            {"user_id": 5, "name": "Marwan", "mail": "quarz#2020@leetcode.com"},
            {"user_id": 6, "name": "David", "mail": "david69@gmail.com"},
            {"user_id": 7, "name": "Shapiro", "mail": ".shapo@leetcode.com"}
        ]
        users = pd.DataFrame(data)
        users = users[users['mail'].str.match(r"^[a-zA-Z][a-zA-Z0-9\_\-\.]*@leetcode\.com$")]
        print(users)

    def find_patients(self) -> pd.DataFrame:
        data = {
            "patient_id": [1, 2, 3, 4, 5],
            "patient_name": ["Daniel", "Alice", "Bob", "George", "Alain"],
            "conditions": ["YFEV COUGH", "", "DIAB100 MYOP", "ACNE DIAB100", "DIAB201"]
        }

        # Create a DataFrame
        patients = pd.DataFrame(data)
        df = patients[patients['conditions'].str.contains(r"\bDIAB1[0-9]*\b")]
        print(df)
    def nth_highest_salary(self, n) -> pd.DataFrame:
        data_dict = {
            "id": [1, 2, 3],
            "salary": [1, 0, 0]
        }
        df = pd.DataFrame(data_dict)
        df = df['salary'].sort_values(ascending=False).unique()
        col = f'getNthHighestSalary({n})'
        if n <= len(df) & n > 0 & isinstance(n, int):
            return pd.DataFrame({col: df[n - 1]}, index=[0])
        else:
            return pd.DataFrame({col: None}, index=[0])

    def second_highest_salary(self) -> pd.DataFrame:
        data_dict = {
            "id": [1, 2],
            "salary": [0, 0]
        }
        df = pd.DataFrame(data_dict)
        df = df['salary'].sort_values(ascending=False).unique()
        if len(df) < 2:
            return pd.DataFrame({'SecondHighestSalary': [None]})
        return pd.DataFrame({'SecondHighestSalary': [df[1]]})

    def department_highest_salary(self) -> pd.DataFrame:
        employee_data = {
            'id': [1, 2, 3, 4, 5],
            'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
            'salary': [70000, 90000, 80000, 60000, 90000],
            'departmentId': [1, 1, 2, 2, 1]
        }
        department_data = {
            'id': [1, 2],
            'name': ['IT', 'Sales']
        }

        employee, department = pd.DataFrame(employee_data), pd.DataFrame(department_data)
        cols_to_keep = {'name_emp': 'Employee', 'name_dpt': 'Department', 'salary': 'Salary'}
        merged_df = pd.merge(left=employee, left_on='departmentId', right=department, right_on='id', how='inner', suffixes=('_emp', '_dpt'))
        grouped_df = merged_df.groupby('departmentId')
        df = grouped_df.apply(lambda x: x[x['salary'] == x['salary'].max()])
        df.reset_index(drop=True, inplace=True)
        df = df.rename(columns=cols_to_keep)[cols_to_keep.values()]
        return df

    def order_scores(self) -> pd.DataFrame:
        data = {
            'id': [1, 2, 3, 4, 5, 6],
            'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
        }
        scores = pd.DataFrame(data)
        llist = scores['score'].unique().tolist()
        llist.sort(reverse=True)
        # max_score = scores['score'].max()
        df = scores[['score']]
        df['rank'] = 0
        count = 1
        while llist:
            max_score = max(llist)
            df.loc[df['score'] == max_score, 'rank'] = count
            count += 1
            llist.remove(max_score)
        df = df.sort_values(by='score', ascending=False)
        print(df)

    def order_scores_2(self):
        data = {
            'id': [1, 2, 3, 4, 5, 6],
            'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
        }
        scores = pd.DataFrame(data)
        scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
        return scores[['score', 'rank']].sort_values(by='score', ascending=False)

    def rearrange_products_table(self) -> pd.DataFrame:
        products_data = {
            'product_id': [0, 1],
            'store1': [95, 70],
            'store2': [100, None],
            'store3': [105, 80]
        }
        products = pd.DataFrame(products_data)
        df = pd.melt(products, id_vars='product_id', var_name='store', value_name='price').dropna()
        return df

    def get_student_name(self):
        students_data = {
            'id': [1, 2, 3, 4, 5],
            'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
            'subject': ['Math', 'Science', 'History', 'Math', 'Science'],
            'marks': [85, 92, 78, 90, 88]
        }
        df = pd.DataFrame(students_data)
        name = df.loc[df['id']==2, 'name'].values[0]
        return name

if __name__ == '__main__':
    sol = Solution()
    # sol.big_countries()
    # sol.find_customers()
    # sol.find_customersII()
    # sol.article_views()
    # sol.invalid_tweets()
    # sol.calculate_special_bonus()
    # sol.valid_emails()
    # sol.find_patients()
    # print(sol.nth_highest_salary(1))
    # print(sol.second_highest_salary())
    # print(sol.department_highest_salary())
    # sol.order_scores()
    # print('different approach')
    # print(sol.order_scores_2())
    # print(sol.rearrange_products_table())

    print(sol.get_student_name())