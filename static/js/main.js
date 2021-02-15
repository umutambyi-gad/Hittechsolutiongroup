AOS.init({
    duration: 800,
    easing: 'slide'
});

(function($) {

    "use strict";

    var fullHeight = function() {

        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function() {
            $('.js-fullheight').css('height', $(window).height());
        });

    };
    fullHeight();

    // loader
    var loader = function() {
        setTimeout(function() {
            if ($('#ftco-loader').length > 0) {
                $('#ftco-loader').removeClass('show');
            }
        }, 1);
    };
    loader();

    // Scrollax
    $.Scrollax();

    var carousel = function() {
        $('.home-slider').owlCarousel({
            loop: true,
            autoplay: true,
            margin: 0,
            animateOut: 'fadeOut',
            animateIn: 'fadeIn',
            nav: false,
            autoplayHoverPause: false,
            items: 1,
            navText: ["<span class='ion-md-arrow-back'></span>", "<span class='ion-chevron-right'></span>"],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 1
                }
            }
        });
        $('.carousel-testimony').owlCarousel({
            autoplay: true,
            center: true,
            loop: true,
            items: 1,
            margin: 30,
            stagePadding: 0,
            nav: false,
            navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1000: {
                    items: 2
                }
            }
        });

    };
    carousel();

    $('nav .dropdown').hover(function() {
        var $this = $(this);
        // 	 timer;
        // clearTimeout(timer);
        $this.addClass('show');
        $this.find('> a').attr('aria-expanded', true);
        // $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
        $this.find('.dropdown-menu').addClass('show');
    }, function() {
        var $this = $(this);
        // timer;
        // timer = setTimeout(function(){
        $this.removeClass('show');
        $this.find('> a').attr('aria-expanded', false);
        // $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
        $this.find('.dropdown-menu').removeClass('show');
        // }, 100);
    });


    $('#dropdown04').on('show.bs.dropdown', function() {
        console.log('show');
    });

    // scroll
    var scrollWindow = function() {
        $(window).scroll(function() {
            var $w = $(this),
                st = $w.scrollTop(),
                navbar = $('.ftco_navbar'),
                sd = $('.js-scroll-wrap');

            if (st > 150) {
                if (!navbar.hasClass('scrolled')) {
                    navbar.addClass('scrolled');
                }
            }
            if (st < 150) {
                if (navbar.hasClass('scrolled')) {
                    navbar.removeClass('scrolled sleep');
                }
            }
            if (st > 350) {
                if (!navbar.hasClass('awake')) {
                    navbar.addClass('awake');
                }

                if (sd.length > 0) {
                    sd.addClass('sleep');
                }
            }
            if (st < 350) {
                if (navbar.hasClass('awake')) {
                    navbar.removeClass('awake');
                    navbar.addClass('sleep');
                }
                if (sd.length > 0) {
                    sd.removeClass('sleep');
                }
            }
        });
    };
    scrollWindow();


    var counter = function() {

        $('#section-counter').waypoint(function(direction) {

            if (direction === 'down' && !$(this.element).hasClass('ftco-animated')) {

                var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
                $('.number').each(function() {
                    var $this = $(this),
                        num = $this.data('number');
                    console.log(num);
                    $this.animateNumber({
                        number: num,
                        numberStep: comma_separator_number_step
                    }, 7000);
                });

            }

        }, {
            offset: '95%'
        });

    }
    counter();

    var contentWayPoint = function() {
        var i = 0;
        $('.ftco-animate').waypoint(function(direction) {

            if (direction === 'down' && !$(this.element).hasClass('ftco-animated')) {

                i++;

                $(this.element).addClass('item-animate');
                setTimeout(function() {

                    $('body .ftco-animate.item-animate').each(function(k) {
                        var el = $(this);
                        setTimeout(function() {
                            var effect = el.data('animate-effect');
                            if (effect === 'fadeIn') {
                                el.addClass('fadeIn ftco-animated');
                            } else if (effect === 'fadeInLeft') {
                                el.addClass('fadeInLeft ftco-animated');
                            } else if (effect === 'fadeInRight') {
                                el.addClass('fadeInRight ftco-animated');
                            } else {
                                el.addClass('fadeInUp ftco-animated');
                            }
                            el.removeClass('item-animate');
                        }, k * 50, 'easeInOutExpo');
                    });

                }, 100);

            }

        }, {
            offset: '95%'
        });
    };
    contentWayPoint();


    // magnific popup
    $('.image-popup').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        closeBtnInside: false,
        fixedContentPos: true,
        mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            verticalFit: true
        },
        zoom: {
            enabled: true,
            duration: 300 // don't foget to change the duration also in CSS
        }
    });

    /* hide replies by default since the user clicks show reply to see it */
    $('.showReplies').on('click', function() {
        $(this).parents().nextAll('ul.children').fadeToggle();
        if ($(this).text() == 'Show replies') {
            $(this).text('Hide replies');
        } else {
            $(this).text('Show replies');
        }
    });


    $('#join').on('click', () => {
        $('.signin-section').fadeIn();
    });

    $('#close-signin').on('click', () => {
        $('.signin-section').fadeOut();
    });
    $('#close-signup').on('click', () => {
        $('.signup-section').fadeOut();
    });

    $('#signup').on('click', () => {
        $('.signin-section').fadeOut();
        $('.signup-section').fadeIn();
    });

    $('#signin').on('click', () => {
        $('.signup-section').fadeOut();
        $('.signin-section').fadeIn();
    });

    /* function for ajax request */
    function ajaxRequest(method, data, success) {
        if (method.toUpperCase() == 'POST') {
            data['csrfmiddlewaretoken'] = $('input[name=csrfmiddlewaretoken]').val();
        }
        $.ajax({
            url: location.path,
            type: method,
            data: data,
            success: success
        });
    }

    let testimony_section = $('.testimony-section');
    $('form.appointment-form').on('submit', function(event) {
        let data = {
            message: $(this).find('.form-group textarea').val().trim()
        };
        let success = response => {
            console.log(response);
            if (response.isUpdate) {
                let id = response.user_id;
                let item = testimony_section.find(`.item.${id}`);
                item.find(`.message.${id}`).text(response.message);
            }
        }
        ajaxRequest('POST', data, success);
        $(this).find('.form-group textarea').val('');
        event.preventDefault();
    });


    let signin_section = $('.signin-section form');

    /* adding loading gif when user is typing username */
    signin_section.find('input[name=username]').on('input', function() {
        $(this).parents().prev('.loading').addClass('active');
    });

    /* adding loading gif when user is typing password */
    signin_section.find('input[name=password]').on('input', function() {
        $(this).parents().prev('.loading').addClass('active');
    });

    /* function for making an input loose fucus */
    function looseFocus(inputSelection) {
        inputSelection.blur();
    }

    /* blur username input if all is not null on Enter keypress to make an ajax request sent */
    signin_section.find('input[name=username]').on('keydown', function(event) {
        if ((event.keyCode == 13) && $(this).val().trim() != '' &&
            signin_section.find('input[name=password]').val().trim() != '') {
            looseFocus($(this));
        }

    });

    /* blur password input if all is not null on Enter keypress to make an ajax request sent */
    signin_section.find('input[name=password]').on('keydown', function(event) {
        if (event.keyCode == 13 && $(this).val().trim() != '' &&
            signin_section.find('input[name=username]').val().trim() != '') {
            looseFocus($(this));
        }
        //
    });

    /* check if data are valid and trigger Enter key to submit the form (login) */
    $(document).on('keydown', function(event) {
        if ((event.keyCode == 13) &&
            ($('.signin-section').css('display') === 'block') &&
            (signin_section.find('input[name=password]').val().trim() != '') &&
            (signin_section.find('input[name=username]').val().trim() != '') &&
            !(signin_section.find('.error-pop-up').hasClass('active')) &&
            !(signin_section.find('input[name=username]').parents().prev('.loading').hasClass('active')) &&
            !(signin_section.find('input[name=password]').parents().prev('.loading').hasClass('active'))) {
            signin_section.submit();
        }
    });

    /* When password input looses focus and password is not null send ajax request to uthenticate */
    signin_section.find('input[name=password]').on('blur', function(event) {
        if (signin_section.find('input[name=username]').val().trim() != '') {
            if ($(this).val().trim() != '') {
                let data = {
                    __username: signin_section.find('input[name=username]').val(),
                    __password: $(this).val()
                };
                let success = response => {
                    if (response.res === 'invalid credentials') {
                        signin_section.find('.error-pop-up').addClass('active').fadeIn(1000);
                    } else {
                        signin_section.find('.error-pop-up').removeClass('active').fadeOut(1000);
                    }
                    signin_section.find('input[name=username]').parents().prev('.loading').removeClass('active');
                    signin_section.find('input[name=password]').parents().prev('.loading').removeClass('active');
                }
                ajaxRequest('POST', data, success);
            }
        }
    });

    /* When username input looses focus and password is not null send ajax request to uthenticate */
    signin_section.find('input[name=username]').on('blur', function(event) {
        if (signin_section.find('input[name=password]').val().trim() != '') {
            if ($(this).val().trim() != '') {
                let data = {
                    __username: $(this).val(),
                    __password: signin_section.find('input[name=password]').val()
                };
                let success = response => {
                    if (response.res === 'invalid credentials') {
                        signin_section.find('.error-pop-up').addClass('active').fadeIn(1000);
                    } else {
                        signin_section.find('.error-pop-up').removeClass('active').fadeOut(1000);
                    }
                    signin_section.find('input[name=username]').parents().prev('.loading').removeClass('active');
                    signin_section.find('input[name=password]').parents().prev('.loading').removeClass('active');
                }
                ajaxRequest('POST', data, success);
            }
        }
    });

    /* When there is an error pop up or response is not yet given by ajax request disable to submit(login) */
    signin_section.on('submit', event => {
        if (signin_section.find('.error-pop-up').hasClass('active') ||
            signin_section.find('input[name=username]').parents().prev('.loading').hasClass('active') ||
            signin_section.find('input[name=password]').parents().prev('.loading').hasClass('active')
        ) {
            event.preventDefault();
        }
    });


    let signup_section_username = $('.signup-section input[name=username]');

    signup_section_username.on('input', function() {
        $(this).parents().prev('.loading').addClass('active');
    });
    /* check if username exists when signing up */
    signup_section_username.on('blur', () => {
        let data = {
            _username: signup_section_username.val()
        }
        let success = response => {
            if (response.existance === 'exists') {
                signup_section_username.parents().next('.error-pop-up').addClass('active').fadeIn(1000);
            } else {
                signup_section_username.parents().next('.error-pop-up').removeClass('active').fadeOut(1000);
            }
            signup_section_username.parents().prev('.loading').removeClass('active');
        }
        ajaxRequest('POST', data, success)
    });

    /* If username already exists disable to submit(sign up) */
    $('.signup-section form').on('submit', event => {
        if (signup_section_username.parents().next('.error-pop-up').hasClass('active') ||
            signup_section_username.parents().prev('.loading').hasClass('active')) {
            event.preventDefault();
        }
    });


    let signup_section_email = $('.signup-section input[name=email]');

    signup_section_email.on('input', function() {
        $(this).parents().prev('.loading').addClass('active');
    });

    /* check if email exists when signing up */
    signup_section_email.on('blur', () => {
        let data = {
            _email: signup_section_email.val()
        }
        let success = response => {
            if (response.existance === 'exists') {
                signup_section_email.parents().next('.error-pop-up').addClass('active').fadeIn(1000);
            } else {
                signup_section_email.parents().next('.error-pop-up').removeClass('active').fadeOut(1000);
            }
            signup_section_email.parents().prev('.loading').removeClass('active');
        }
        ajaxRequest('POST', data, success)
    });

    /* If emain already exists or the response is not yet given by an ajax request disable to submit(sign up) */
    $('.signup-section form').on('submit', event => {
        if (signup_section_email.parents().next('.error-pop-up').hasClass('active') ||
            signup_section_email.parents().prev('.loading').hasClass('active')) {
            event.preventDefault();
        }
    });


    let profileset = $('#profileset form');

    /* check If username already exists when updating the profile */
    profileset.find('input[name=username]').on('input', function(event) {
        let data = {
            _username: $(this).val()
        }
        let success = response => {
            if (response.existance === 'exists') {
                $(this).parents().next('.error-pop-up').addClass('active').fadeIn(1000);
            } else {
                $(this).parents().next('.error-pop-up').removeClass('active').fadeOut(1000);
            }
        }
        ajaxRequest('POST', data, success);
    });

    /* check If email already exists when updating the profile */
    profileset.find('input[name=email]').on('input', function(event) {
        let data = {
            _email: $(this).val()
        }
        let success = response => {
            if (response.existance === 'exists') {
                $(this).parents().next('.error-pop-up').addClass('active').fadeIn(1000);
            } else {
                $(this).parents().next('.error-pop-up').removeClass('active').fadeOut(1000);
            }
        }
        ajaxRequest('POST', data, success);
    });

    /* If email or username already exists disable to submit(updating profile) */
    profileset.on('submit', event => {
        if (profileset.find('input[name=username]').parents().next('.error-pop-up').hasClass('active') ||
            profileset.find('input[name=email]').parents().next('.error-pop-up').hasClass('active')) {
            event.preventDefault();
        }
    });


    /* if passwords are not matching disable to submit the form */
    $('#sign-up-section').on('submit', event => {
        if ($('.pwd_1').val().trim() != $('.pwd_2').val().trim()) {
            $('.pwd_1').parents().next('.error-pop-up').fadeIn(1000);
            $('.pwd_2').parents().next('.error-pop-up').fadeIn(1000);
            event.preventDefault();
        } else {
            $('.pwd_1').parents().next('.error-pop-up').fadeOut(1000);
            $('.pwd_2').parents().next('.error-pop-up').fadeOut(1000);
        }
    });

    /* Get the id of clicked button(reply button in the comment) */
    $('.reply').on('click', function() {
        /* if user is not authenticated take him/her to the login page */
        if ($(this).hasClass('notAuthenticated')) {
            $('.signin-section').fadeIn(1000);
        } else {
            /* get the name of who going be replied to for formating it like '@username' */
            let commentor = $(this).parents('.comment-body').children('h3').text().trim();
            /* get the id which is the second class of the reply button */
            let id = $(this).attr('class').split(' ')[1];
            sessionStorage.clear();
            sessionStorage.setItem('root_comment_id', id);
            $('#message').val(`@${commentor} `);
        }
    });


    $(window).on('load', () => sessionStorage.clear());


    $('#message').on('input', function() {
        sessionStorage.setItem('ajax_message', $(this).val())
    });


    /* send the comment if its reply send it with an id of replied comment */
    $('#postcomment').on('click', function() {
        if ($(this).hasClass('notAuthenticated')) {
            $('.signin-section').fadeIn(1000);
        } else {
            let data = {
                ajax_message: sessionStorage.getItem('ajax_message'),
                root_comment_id: sessionStorage.getItem('root_comment_id'),
            };
            let success = response => {
                sessionStorage.clear();
                location.reload();
            }
            ajaxRequest('POST', data, success);
        }
    });



    $('#profile').on('click', () => {
        $('#profileset').fadeIn();
    });

    $('#close-profileset').on('click', () => {
        $('#profileset').fadeOut();
    });


    $(window).on('load', () => {
        if ($('#notification-bar > p').text().trim().length > 0) {
            $('#notification-bar').fadeIn(1000);
            setTimeout(() => $('#notification-bar').fadeOut(1000), 6000);
        }
    });


    /* delete root comment */
    $('.delete-root').on('click', function() {
        let data = {
            root_id: $(this).attr('class').split(' ')[1]
        };
        let success = response => {
            $('h3 span.total').text(response.total_comments);
            $('a span.total').text(response.total_comments);
            $(this).parents('li.comment').remove();
        }
        ajaxRequest('POST', data, success);
    });

    /* delete reply comment */
    $('.delete-reply').on('click', function() {
        let data = {
            reply_id: $(this).attr('class').split(' ')[1]
        };
        let success = response => {
            $(this).parents('ul.children').remove();
        }
        ajaxRequest('POST', data, success);
    });

})(jQuery);