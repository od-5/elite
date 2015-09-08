/**
 * Created by alexy on 28.05.15.
 */
$(function() {
  //$('.popupbutton').fancybox({
  //  'padding': 37,
  //  'overlayOpacity': 0.87,
  //  'overlayColor': '#fff',
  //  'transitionIn': 'none',
  //  'transitionOut': 'none',
  //  'titlePosition': 'inside',
  //  'centerOnScroll': true,
  //  'width': 600,
  //  'minHeight': 310,
  //  afterClose: function(e){
  //    $('.ticket-form').trigger('reset');
  //  }
  //});
  //
  //$('.popupbutton').on('click', function(e){
  //  var form = $(this).parent('form');
  //  var name = form.find('.ticket-form__name').val();
  //  var email = form.find('.ticket-form__email').val();
  //  $('.pop-form').find('.ticket-form__name__travel').val(name)
  //  $('.pop-form').find('.ticket-form__email__travel').val(email)
  //});
  //
  //$( ".pop-form" ).validate({
  //  rules: {
  //    name: {
  //      required: true
  //    },
  //    email: {
  //      required: true
  //    }
  //  },
  //  submitHandler: function(e) {
  //    $('.pop-form').ajaxSubmit({
  //        success: function(data){
  //          $.fancybox.close();
  //        }
  //    });
  //  }
  //});
  $.validator.messages.required = "* поле обязательно для заполнения";
  $( "header form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('header form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });

  $( "footer form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('footer form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('form').trigger('reset');
          }
      });
    }
  });

  $('.section-address-container-item-link').hover(function(){
    $(this).find('.section-address-container-item-link-back').toggle();
  });

  $('.flexslider').flexslider({
    animation: "slide"
  });

  $('.section-advantage-button, .section-address-ticket-button').on('click', function(e){
    $('#pop').fadeIn();
    $('body').append('<div class="overlay"></div>');
  });
  $('.modal-close').on('click', function(e){
    //alert('ok');
    $('#pop').fadeOut();
    $('.overlay').remove();
  });

  $( "#pop form" ).validate({
    rules: {
      name: {
        required: true
      },
      phone: {
        required: true
      }
    },
    submitHandler: function(e) {
      $('#pop form').ajaxSubmit({
          success: function(data){
            if (data.success) {
              $.notify('Ваша заявка принята!', 'success');
            } else {
              $.notify('Что то пошло не так', 'error');
            }
            $('#pop form').trigger('reset');
            $('#pop').fadeOut();
            $('.overlay').remove();
          }
      });
    }
  });

});