/**
 * Created by alexy on 28.05.15.
 */
$(function() {

  var current_url = '/'+location.href.split('/')[3]+'/'
  $('.nav-list-item__link').each(function () {
    if($(this).attr('href') == current_url) $(this).addClass('nav-list-item__link_active');
  });

  $(document).on('click', 'a[href^=#]', function () {
      $('html, body').animate({ scrollTop:  $('a[name="'+this.hash.slice(1)+'"]').offset().top }, 300 );
      return false;
  });

  $('section').addClass("hidden").viewportChecker({
    classToAdd: 'visible animated fadeIn',
    offset: 100
  });
  $('.section-video-container, .section-advantage-list').addClass("hidden").viewportChecker({
    classToAdd: 'visible animated fadeIn',
    offset: 200
  });

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


  $('.section-advantage-button, .section-address-ticket-button, .section-video-ticket-button').on('click', function(e){
    $('#pop').fadeIn();
    $('body').append('<div class="overlay"></div>');
  });
  $('.section-address-container-item-link').on('click', function(e){
    $.ajax({
      type: "POST",
      url: $(this).data('url'),
      data: {
        'address': $(this).data('address')
      },
      success: function(msg){
        //alert( "Прибыли данные: " + msg.success[0] );
        var address_list = msg.success;
        $('.pop-gallery').append('<div class="gallery"><ul class="slides"></ul></div>');
        for (var i = 0; i < address_list.length; i++) {
          console.log(address_list[i]);
          $('.gallery .slides').append('<li><img src=' + address_list[i] + '></li>');
        }
        $('.gallery').flexslider({
          animation: "slide"
        });
      }
    });
    $('.pop-gallery').fadeIn();
    $('body').append('<div class="overlay"></div>');

  });

  $('.modal-close').on('click', function(e){
    //alert('ok');
    $('#pop').fadeOut();
    $('.pop-gallery').fadeOut();
    if ($('.gallery .slides li').length) {
      $('.gallery').detach();
    }
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