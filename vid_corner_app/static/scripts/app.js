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

    var urlEndpoint = `http://localhost:8000/video/${videoId}/like`

    $.ajax({
        method: "POST",
        url: urlEndpoint,
        data: theScoop,
        success: function likeSucess(json) {
            console.log(json)
        }
    })
})

