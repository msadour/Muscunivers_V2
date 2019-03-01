$('.button_share').click(function(){
    var message = $('#message_publication_form').val()

    $.ajax({
        url : '/publish_to_wall',
        dataType : 'json',
        data: {
          'message': message
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

$('.icon_delete').click(function(){
    id_publication = $(this).closest("form").attr('id');

    $.ajax({
        url : '/delete_status',
        dataType : 'json',
        data: {
          'id_publication': id_publication
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

$('.icon_delete_comment').click(function(){
    id_publication = $(this).closest("form").attr('id');

    $.ajax({
        url : '/delete_comment',
        dataType : 'json',
        data: {
          'id_publication': id_publication
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})


$('.button_comment').click(function(){
    comment = $(this).closest("form").find('textarea').val()
    id_status = $(this).closest("form").attr('name');
    console.log('----------------------')
    console.log(id_status)
    console.log('----------------------')

    $.ajax({
        url : '/comment_status',
        dataType : 'json',
        data: {
          'comment': comment,
          'id_status': id_status
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

$('.icon_delete_comment').click(function(){
    id_publication = $(this).closest("form").attr('id');

    $.ajax({
        url : '/delete_comment',
        dataType : 'json',
        data: {
          'id_publication': id_publication
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

// Coaching

$('.icon_delete_coaching').click(function(){
    id_coaching = $(this).closest("form").attr('id');

    $.ajax({
        url : '/delete_coaching',
        dataType : 'json',
        data: {
          'id_coaching': id_coaching
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

// Product

$('.icon_delete_product').click(function(){
    id_product = $(this).closest("form").attr('id');
    console.log('***************')
    console.log(id_product)
    console.log('***************')

    $.ajax({
        url : '/delete_product',
        dataType : 'json',
        data: {
          'id_product': id_product
        },

        success : function(response){
            console.log('Success')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

