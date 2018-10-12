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
            console.log(json)
            if(json.likes.length !== 0) {
                $('.videoLike').addClass('likeColor')
            }
            
            else if (json.likes.length === 0) {
                
                $.ajax({
                    method: "DELETE",
                    url: deleteEndpoint,
                    data: theScoop,
                    success: function deleteSuccess(response) {
                        
                        $('.videoLike').removeClass('likeColor')
                        console.log('already liked so deleting')
                    }
                })
            }
            
        }
    })
})




$('.videoDislike').on('click', function(e) {
    var form = $('.likeForm').serialize()
    var videoId = $('.videoId').attr('value')
    var user = $('.user').attr('value')

    var dislikeInfo = {
        form: form,
        videoId: videoId,
        user: user
    }

    console.log(dislikeInfo)
    var dislikeEndpoint = `http://localhost:8000/video/${videoId}/dislike`
    var deleteEndpoint = `http://localhost:8000/video/${videoId}/dislike/delete`
    e.preventDefault()


$.ajax({
    method: "POST",
    url: dislikeEndpoint,
    data: dislikeInfo,
    success: function dislikeSuccess(json) {
        console.log(json)
        if (json.dislikes.length !== 0) {
            $('.videoDislike').addClass('likeColor')
        }
        else if (json.dislikes.length === 0) {
            $('.videoDislike').removeClass('likeColor')
            $.ajax({
                method: "DELETE",
                url: deleteEndpoint,
                data: dislikeInfo,
                success: function deleteSuccess(response) {
                    $('.videoDislike').removeClass('likeColor')
                    console.log('already disliked so deleting dislike')
                }
            })
        }
    },
})

})

