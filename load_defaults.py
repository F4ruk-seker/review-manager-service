from comment.models import CommentTag, CommentTagColor


CommentTag().load_built_in_tags()

CommentTagColor().load_built_in_colors()
