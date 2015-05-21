from models import Posts
import logging


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
        logger = logging.getLogger("stuff")
      
        if all_children.count() > 0:          
            self.children = []
            
            for child in all_children:
                self.children.append(post_tree(child.post_id, self))

        else:
            self.children = None
            
    '''     
    

    public function display_posts(){

        // All of the posts have a parent node. The top level posts have a root
        // node with no text.

        if($this->post_text != NULL){ // We are not the root node

            // Display the content of this post
            echo "<li name='".$this->post_id."' class='post' id='".$this->post_id."' ><div class='post_div'>";
            echo "<p><strong>".htmlspecialchars($this->username)."</strong> on ".$this->date_posted."</p>"; 


            echo "<p class='post_text'>";

            if($this->deleted == false){
                echo htmlspecialchars($this->post_text);
                echo "<a class='delete_post' href='delete_post.php?post_id=$this->post_id&thread_id=$this->thread_id'>Delete</a>";
            }
            else{ 
                echo "This post has been deleted by the moderator";
            }

            echo "</p>";
            if($this->children == NULL){
                echo "<button type='button' class='reply_new_branch'>Reply to this post</button>";
            }
            echo "</div></li>";
        }

        # Display this post's children
        if($this->children != NULL){
            echo "<ul id='".$this->post_id."'>\r\n";
            for($i = 0; $i < count($this->children) ; $i++){
                $this->children[$i]->display_posts();
            }

            echo "</ul>\r\n";
        }
        else{


        }
        // Add a reply button to add new children 

        if($this->post_text != NULL){
            $num_children = $this->parent->num_children(); 

            if ($this->parent->children[$num_children-1] == $this){ // We are not the root node
                echo "<li>";
                echo "<button type='button' class='reply_current_branch'>Continue conversation</button>";
                echo "</li>";
            }
        }
    }

    public function num_children(){
        return count($this->children);
    }

}


def delete_post($post_id):

    $db = connect_db();

    $post_id_int = intval($post_id);

    $prepared = $db->prepare('update posts set deleted = true where post_id = ?');
    $prepared->bind_param('i',$post_id_int);   
    $prepared->execute();

    $prepared->close();
    $db->close(); 
'''

