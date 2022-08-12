from distutils.log import debug
from flask import Flask
from flask_restful import Api,Resource,reqparse,abort

app=Flask(__name__)
api=Api(app)

video={} #
video_argument=reqparse.RequestParser()
video_argument.add_argument("name",type=str,help="Name of the video is required",required=True)
video_argument.add_argument("likes",type=int,help="Name of the video is required",required=True)
video_argument.add_argument("views",type=int,help="Name of the video is required",required=True)

class Video(Resource):
    def get(self,video_id):
        if video_id==0:
            return video
        return video[video_id]

    def put(self,video_id):
        arg=video_argument.parse_args()
        video[video_id]=arg
        return video[video_id]

    def delete(self,video_id):
        del video[video_id]
        return 1

api.add_resource(Video,"/video/<int:video_id>")

if __name__=="__main__":
    app.run(debug==True)
