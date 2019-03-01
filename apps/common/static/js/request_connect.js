$('.add_button').click(function(){
    var id_user = $(this).attr('name')
    var type_contact = 'add_contact'
    var button = this;

    $.ajax({
        url : '/manage_contact',
        dataType : 'json',
        data: {
          'id_user': id_user,
          'type_contact': type_contact
        },

        success : function(response){
            $(button).replaceWith( "<button value='Request send' class='request_send_button' type='submit' name=" + id_user + "> <img src=\"/static/img/cancel.png\"> Request send </button>" );
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

$('.join_button').click(function(){
    var id_user = $(this).attr('name')
    var type_contact = 'add_employees'
    var button = this;

    $.ajax({
        url : '/manage_contact',
        dataType : 'json',
        data: {
          'id_user': id_user,
          'type_contact': type_contact
        },

        success : function(response){
            $(button).replaceWith( "<button value='Request send' class='request_send_button' type='submit' name=" + id_user + "> <img src=\"/static/img/cancel.png\"> Request send </button>" );
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

$('.request_send_button').click(function(){
    var id_user = $(this).attr('name')
    var type_contact = 'cancel_request'
    var button = this;
    $.ajax({
        url : '/manage_contact',
        dataType : 'json',
        data: {
          'id_user': id_user,
          'type_contact': type_contact
        },

        success : function(response){
            $(button).replaceWith( "<button value='add' class='add_button' type='submit' name=" + id_user + " > <img src=\"/static/img/add.png\"> Add </button>" );
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})


$('.accept_button').click(function(){
    var id_user = $(this).attr('name')
    var type_contact = 'accept'

    $.ajax({
        url : '/accept_or_decline',
        dataType : 'json',
        data: {
          'id_user': id_user,
          'type_contact': type_contact
        },

        success : function(response){
            console.log("ok");
            $('#' + id_user).css('display', 'none')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})


$('.decline_button').click(function(){
    var id_user = $(this).attr('name')
    var type_contact = 'decline'
    $.ajax({
        url : '/accept_or_decline',
        dataType : 'json',
        data: {
          'id_user': id_user,
          'type_contact': type_contact
        },

        success : function(response){
            console.log("ok");
            $('#' + id_user).css('display', 'none')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

$('.remove_friend_button').click(function(){
    var id_user = $(this).attr('name')

    $.ajax({
        url : '/remove_contact',
        dataType : 'json',
        data: {
          'id_user': id_user
        },

        success : function(response){
            console.log("ok");
            $('#' + id_user).css('display', 'none')
        },
        error: function(error) {
            console.log('******************')
            console.log(error)
        }
    });
})

//<button value="add" type="submit" class="add_button" name="{{result.0.user.id}}">
//                            <img src="{% static 'img/add.png' %}"> Add </button>