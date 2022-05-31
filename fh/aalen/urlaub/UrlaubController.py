class UrlaubController:

    def __init__(self, app, res):
        self.app=app
        self.res=res

        # Calls method on_get_persons
        self.app.add_route('/urlaubswuensche', self.res, suffix='urlaubswuensche')
        # Calls methods on_get_person to get a single person by id
        # on_put_video to update a video and on_delete to delete a video
        self.app.add_route('/urlaubswunsch/{id}', self.res, suffix='urlaubswunsch')
        # Calls method on_post_person
        self.app.add_route('/urlaubswunsch', self.res, suffix='urlaubswunsch')
        #Get Video by title
        #self.app.add_route('/videotitle/{title}', self.res, suffix='videotitle')
        self.app.add_route('/urlaubswunschfavourite/{urlaubswunsch_id}/{urlaub_id}', self.res, suffix='addurlaubswunschfavourite')
        # A route to a static content directory, e.g. html files
        self.app.add_static_route('/', '/Users/Sina/PycharmProjects/Urlaubsplanung/')