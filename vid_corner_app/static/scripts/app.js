$('.videoLike').on('click', function(e) {
    e.preventDefault()
    var form = $('.likeForm').serialize()
    var videoId = $('.videoId').attr('value')
    var user = $('.user').attr('value')
    
    var theScoop = {
        form: form,
        videoId: videoId,
        user: user
    }

    var likeEndpoint = `http://localhost:8000/video/${videoId}/like`

    var deleteEndpoint = `http://localhost:8000/video/${videoId}/like/delete`

    $.ajax({
        method: "POST",
        url: likeEndpoint,
        data: theScoop,
        success: function likeSucess(json) {
            if (json.likes.length === 0) {
                $.ajax({
                    method: "DELETE",
                    url: deleteEndpoint,
                    data: theScoop,
                    success: function deleteSuccess(response) {
                        console.log('already liked so deleting')
                    }
                })
            }
            
        }
    })
})

