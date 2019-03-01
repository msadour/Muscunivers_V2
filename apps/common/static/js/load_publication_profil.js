setInterval(function(){
    // -------------------------- Notification --------------------------
    $.ajax({
       url: '/get_new_publications_profil',
          data: {},
          success: function(data) {
            $('#all_publications').html(data);
          }
    });
}, 5000)