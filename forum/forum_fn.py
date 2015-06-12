from models import Posts


class post_tree():


    def __init__(self, new_post_id, parent = None):


        self.post_id = new_post_id


        # Get the post content
        post_object  = Posts.objects.get(post_id = self.post_id)
          
        self.post_text   = post_object.post_text
        self.username    = post_object.username
        self.date_posted = post_object.date_posted
        self.parent_id   = post_object.parent_id
        self.deleted     = post_object.deleted
        self.thread_id   = post_object.thread_id
        self.parent      = parent

        #Get the content any children.
        all_children        = Posts.objects.filter(parent_id = self.post_id).order_by('date_posted')
      
        if all_children.count() > 0:          
            self.children = []
            
            for child in all_children:
                self.children.append(post_tree(child.post_id, self))

        else:
            self.children = None
            
