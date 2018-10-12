


let dislikeVidId;
let dislikeApiUserId;
let likevidId;
let likeApiUserId;
let videoId = $('.videoId').attr('value');
let currentUserId = $('.user').attr('value');


$.ajax({
    method: 'GET',
    url: `http://localhost:8000/api/likes`,
    async: false,
    success: function onSucess(response) {
        response.likes.forEach(function(like) {
            likevidId = like.video
            likeApiUserId = like.user
            if ( videoId == likevidId && currentUserId == likeApiUserId) {
    
                $('.videoLike').addClass('likeColor')
            } else {
                console.log('nope for likes')
            }
                
            
        })
    }
})








$.ajax({
    method: 'GET',
    url: 'http://localhost:8000/api/dislikes',
    async: false,
    success: function dislikeOnSucess(response) {
        console.log(response)
        response.dislikes.forEach(function(dislike) {
            dislikeVidId = dislike.video
            dislikeApiUserId = dislike.user
            if ( videoId == dislikeVidId && currentUserId == dislikeApiUserId) {
    
                $('.videoDislike').addClass('likeColor')
            } else {
                console.log('nope for dislikes')
            }
        })
    }
})




var getType = (function() {

    var objToString = ({}).toString ,
        typeMap     = {},
        types = [ 
          "Boolean", 
          "Number", 
          "String",                
          "Function", 
          "Array", 
          "Date",
          "RegExp", 
          "Object", 
          "Error"
        ];

    for ( var i = 0; i < types.length ; i++ ){
        typeMap[ "[object " + types[i] + "]" ] = types[i].toLowerCase();
    };    

    return function( obj ){
        if ( obj == null ) {
            return String( obj );
        }
        // Support: Safari <= 5.1 (functionish RegExp)
        return typeof obj === "object" || typeof obj === "function" ?
            typeMap[ objToString.call(obj) ] || "object" :
            typeof obj;
    }
}());



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
            // console.log(json)
            if(json.likes.length !== 0) {
                var value = parseInt($('.likeCounter').text())
                $('.likeCounter').text(value + 1)
                $('.videoLike').addClass('likeColor')
            }
            
            else if (json.likes.length === 0) {
                
                $.ajax({
                    method: "DELETE",
                    url: deleteEndpoint,
                    data: theScoop,
                    success: function deleteSuccess(response) {
                        
                        $('.videoLike').removeClass('likeColor')
                        
                        var value = parseInt($('.likeCounter').text())
                        $('.likeCounter').text(value - 1)
                        
                        // console.log('already liked so deleting')
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
            var value = parseInt($('.dislikeCounter').text())
            $('.dislikeCounter').text(value + 1) 
            
            
        }
        else if (json.dislikes.length === 0) {
            $('.videoDislike').removeClass('likeColor')
            $.ajax({
                method: "DELETE",
                url: deleteEndpoint,
                data: dislikeInfo,
                success: function deleteSuccess(response) {
                    $('.videoDislike').removeClass('likeColor')
                    var value = parseInt($('.dislikeCounter').text())
                        $('.dislikeCounter').text(value - 1)
                    
                    
                    console.log('already disliked so deleting dislike')
                }
            })
        }
    },
})

});


