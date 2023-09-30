from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd
from typing import Dict, Union, List

app = Flask(__name__)
api = Api(app)


def load_data(filename='data.csv') -> pd.DataFrame:
    return pd.read_csv(filename)

def save_data(data: pd.DataFrame, filename='data.csv') -> None:
    data.to_csv(filename, index=False)

class Blog(Resource):
    def get(self) -> Dict[str, List[Dict[str, Union[int, str]]]]:
        """
        Retrieve all blog posts.

        Returns:
            A dictionary containing a list of all blog posts.
        """
        data = load_data()
        return {'data': data.to_dict('records')}, 200
    
    def post(self) -> Dict[str, Union[str, int]]:
        args = post_parser.parse_args()
        data = load_data()

        next_id = data['id'].max() + 1 if not data['id'].empty else 1
        new_data = pd.DataFrame([{'id': next_id, 'title': args['title'], 'content': args['content']}])
        data = pd.concat([data, new_data], ignore_index=True)
        
        save_data(data)
        return {'message': f'New blog entry added with id {next_id}'}, 201

    def delete(self) -> Dict[str, str]:
        args = delete_parser.parse_args()
        data = load_data()
        
        if args['id'] in data['id'].values:
            data = data[data['id'] != args['id']]
            save_data(data)
            return {'message': f'Blog post with id {args["id"]} deleted'}, 200
        return {'message': f'No blog post found with id {args["id"]}'}, 404

    def put(self) -> Dict[str, Union[str, int]]:
        args = put_parser.parse_args()
        data = load_data()
        
        if args['id'] in data['id'].values:
            if args['title']:
                data.loc[data['id'] == args['id'], 'title'] = args['title']
            if args['content']:
                data.loc[data['id'] == args['id'], 'content'] = args['content']
            save_data(data)
            return {'message': f'Blog post with id {args["id"]} updated'}, 200
        return {'message': f'No blog post found with id {args["id"]}'}, 404
    
# Initialize parsers
post_parser = reqparse.RequestParser()
post_parser.add_argument('title', type=str, required=True)
post_parser.add_argument('content', type=str, required=True)

delete_parser = reqparse.RequestParser()
delete_parser.add_argument('id', type=int, required=True)

put_parser = reqparse.RequestParser()
put_parser.add_argument('id', type=int, required=True)
put_parser.add_argument('title', type=str)
put_parser.add_argument('content', type=str)

# Routing
api.add_resource(Blog, '/api/v1/blogs')

if __name__ == "__main__":
    app.run(debug=True)