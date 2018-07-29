"use strict";
$.noConflict();
var $ = jQuery;

$(document).ready(function($) {

    /**
     *  Smooth Scroll
     *  -----------------------------------------------------------------------
     *  For All the links smoothly animating to their respective section
     */
    $('.scrollbtn a[href*="#"]:not([href="javascript:void(0)"])').on("click", function() {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, 1000);
                return false;
            }
        }
    });

    /**
     *  Active Menu Js
     *  -----------------------------------------------------------------------
     *  For Navbar Section adding active to selected menu
     */
    $('.navbar-nav li a').on("click", function(e) {
        $('.navbar-nav li').removeClass('active');
        var $parent = $(this).parent();
        if (!$parent.hasClass('active')) {
            $parent.addClass('active');
        }
    });

    /**
     *  Navbar Close Icon
     *  -----------------------------------------------------------------------
     *  For Navbar Section Close Icon
     */
    $(".navbar-toggle").on("click", function() {
        $(this).toggleClass("active");
        $("#header").toggleClass("headClr");
        $("body").toggleClass("popup-open");
    });

    $('.main-menu ul li a').click(function() {
        $("body").removeClass("popup-open");
    });

    /**
     *  Navbar Responsive Js
     *  -----------------------------------------------------------------------
     *  For Navbar Section Responsive Js
     */
    function resMenu() {
        if ($(window).width() < 1200) {
            $('.main-menu ul li a').on("click", function() {
                $(".navbar-collapse").removeClass("in");
                $(".navbar-toggle").addClass("collapsed").removeClass("active");
                $("#header").removeClass("headClr");
            });
        }
    }
    resMenu();

    /**
     *  Back To Top
     *  -----------------------------------------------------------------------
     *  For Back To Top button Js
     */
    var offset = 300,
        offset_opacity = 1200,
        scroll_top_duration = 700,
        $back_to_top = $('.back-to-top');

    $(window).scroll(function() {
        ($(this).scrollTop() > offset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
        if ($(this).scrollTop() > offset_opacity) {
            $back_to_top.addClass('cd-fade-out');
        }

        // On scroll header reduce js  
        var scroll = $(window).scrollTop();
        if (scroll >= 100) {
            $("#header").addClass("fixed");
        } else {
            $("#header").removeClass("fixed");
        }

        if ($(window).width() < 767) {
            $("#header").removeClass("fixed");
        }

    });

    $back_to_top.on('click', function(event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    });

    /**
     *  Menu
     *  -----------------------------------------------------------------------
     *  Menu JS For All Header Other than Center logo
     */
    var responsive_main_menu = {

        main_menu: function() {
            var combined_main_menu = $('#main-menu ul.navbar-nav').clone();
            $(".menu-wrap").append('<a href="javascript:void(0)" class="close"><i class="fa fa-times"></i></a>');
            $(".menu-wrap").append('<a href="index.html" class="menu-logo"> <img src="images/logo-footer.png" alt="images" /> </a>');
            combined_main_menu.appendTo('.menu-wrap');

            var main_items = $('.overlapblackbg, .slideLeft'),
                main_menucontent = $('.main_menucontent'),
                sub_menu = $('.menu-wrap ul li').has('.sub-menu'),
                menu_open = function() {
                    $(main_items).removeClass('menuclose').addClass('menuopen');
                },
                menu_close = function() {
                    $(main_items).removeClass('menuopen').addClass('menuclose');
                };
            $('.navbar-toggle').on('click', function() {
                if (main_menucontent.hasClass('menuopen')) {
                    $(menu_close);
                } else {
                    $(menu_open);
                }
            });
            main_menucontent.on('click', function() {
                if (main_menucontent.hasClass('menuopen')) {
                    $(menu_close);
                }
            });
            $('.navbar-toggle, .overlapblackbg').on('click', function() {
                $('.menu-wrap').toggleClass("move-menu");
                $('.blog-main').toggleClass("move-body");
            });
            if (sub_menu) {
                //$('.sub-menu').prev().append('<span class="fa fa-angle-down"></span>');
            }
            sub_menu.prepend('<span class="menu-click"><i class="menu-arrow fa fa-angle-right"></i></span>');
            $('.menu-wrap .menu-click').on('click', function() {
                $(this).siblings('.sub-menu').slideToggle('slow');
                $(this).children('.menu-arrow').toggleClass('menu-extend');
            });
            $('.menu-wrap .close, .overlapblackbg').on('click', function() {
                $(main_items).removeClass('menuopen').addClass('menuclose');
                $('.menu-wrap').removeClass("move-menu");
                $('.blog-main').removeClass("move-body");
            });
        },

        initializ: function() {
            responsive_main_menu.main_menu();
        }
    };

    responsive_main_menu.main_menu();


    /**
     *  Equal Height
     *  -----------------------------------------------------------------------
     *  For Address Column
     */
    $(".cntct-box").height($(".cntct-box").height());

    /**
     *  Parallax
     *  -----------------------------------------------------------------------
     *  For All the sections with parallax background images
     */
    $('.parallax-fix').each(function() {
        if ($(this).children('.parallax-background-img').length) {
            var imgSrc = jQuery(this).children('.parallax-background-img').attr('src');
            jQuery(this).css('background', 'url("' + imgSrc + '")');
            jQuery(this).children('.parallax-background-img').remove();
            $(this).css('background-position', '50% 0%');
        }

    });
    var IsParallaxGenerated = false;

    function SetParallax() {
        if ($(window).width() > 1030 && !IsParallaxGenerated) {
            $('.parallaximg').parallax("50%", 0.05);
            $('.parallaximg-2').parallax("50%", 0.01);
            IsParallaxGenerated = true;
        }
    }

    SetParallax();

    /**
     *  Full Screen Width/Height Js
     *  -----------------------------------------------------------------------
     *  For Header Banner Section Full screen height/width
     */
    function SetResizeContent() {
        var minheight = $(window).height();
        $(".full-screen-mode").css('min-height', minheight);

        var minwidth = $(window).width();
        $(".full-screen-width-mode").css('min-width', minwidth);
    }

    SetResizeContent();

    /**
     *  Owl Carousel
     *  -----------------------------------------------------------------------
     *  For Main banner slider
     */
    $(".banner-slider").owlCarousel({
        navigation: true,
        items: 1,
        merge: true,
        loop: true,
        video: true,
        lazyLoad: true,
        center: true,
        itemsDesktop: false,
        itemsDesktopSmall: false,
        itemsTablet: false,
        itemsMobile: false,
        pagination: false
    });

    /**
     *  Owl Carousel
     *  -----------------------------------------------------------------------
     *  For Image Slider Page
     */
    $(".imgSlider").owlCarousel({
        navigation: true,
        items: 1,
        merge: true,
        loop: true,
        video: true,
        lazyLoad: true,
        center: true,
        itemsDesktop: false,
        itemsDesktopSmall: false,
        itemsTablet: false,
        itemsMobile: false,
        pagination: false
    });

    /**
     *  Call Masonry.
     *  -----------------------------------------------------------------------
     *  For Blog Masonry & Blog Grid Section - Masonry Grid
     */
    $('.blog_grid_masonry').imagesLoaded(function() {
        $('.blog_grid_masonry').masonry({

            columnWidth: '.outer-blog-box',
            itemSelector: '.outer-blog-box',
            gutter: 0

        });
    });


    /**
     *  Magnific popup.
     *  -----------------------------------------------------------------------
     *  For thumb Gallery Section Popup
     */
    $('#popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'blog-media',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
        }
    });

    /**
     *  Owl Carousel
     *  -----------------------------------------------------------------------
     *  For instagram slider
     */
    $('#footer-instagram-feed').owlCarousel({
        items: 10,
        loop: true,
        mouseDrag: true,
        nav: false,
        margin: 2,
        dots: false,
        responsive: {
            1200: {
                items: 10
            },
            1000: {
                items: 7
            },
            600: {
                items: 5
            },
            200: {
                items: 3
            }
        }
    });

    /**
     *  Equal Height
     *  -----------------------------------------------------------------------
     *  For Address Column On resize
     */
    $(window).on('resize', function() {
        $(".cntct-box").height($(".cntct-box").height());
    });

    /**
     *  Map Cursor
     *  -----------------------------------------------------------------------
     *  For Map Cursor JS
     */
    $('#map').click(function() {
        $('#map iframe').css("pointer-events", "auto");
    });

    $("#map").mouseleave(function() {
        $('#map iframe').css("pointer-events", "none");
    });

    /**
     *  Menu
     *  -----------------------------------------------------------------------
     *  Menu JS For Header with Center Logo
     */

    var responsive_menu = {
        /* ---------------------------------------------
         Menu
         --------------------------------------------- */
        menu: function() {
            var combinedmenu = $('#nav-left ul.menu-list').clone(),
                secondmenu = $('#nav-right ul.menu-list').clone(),
                search_menu = $('.site-navigation .search-form').clone();

            secondmenu.children('li').appendTo(combinedmenu);
            $("#mobile-menu-wrap").append('<a href="javascript:void(0)" class="close"><i class="fa fa-times"></i></a>');
            $("#mobile-menu-wrap").append('<a href="index.html" class="menu-logo"> <img src="images/logo-footer.png" alt="images" /> </a>');
            search_menu.appendTo('.mobile-search-form');
            combinedmenu.appendTo('#mobile-menu-wrap');

            var items = $('.overlapblackbg, .slideLeft'),
                menucontent = $('.menucontent'),
                submenu = $('.menu-list li').has('.sub-menu'),
                menuopen = function() {
                    $(items).removeClass('menuclose').addClass('menuopen');
                },
                menuclose = function() {
                    $(items).removeClass('menuopen').addClass('menuclose');
                };
            $('#navToggle').on('click', function() {
                if (menucontent.hasClass('menuopen')) {
                    $(menuclose);
                } else {
                    $(menuopen);
                }
            });
            menucontent.on('click', function() {
                if (menucontent.hasClass('menuopen')) {
                    $(menuclose);
                }
            });
            $('#navToggle, .overlapblackbg').on('click', function() {
                $('#mobile-menu').toggleClass("move-menu");
                $('.blog-main').toggleClass("move-body");
            });
            if (submenu) {
                //$('.sub-menu').prev().append('<span class="fa fa-angle-down"></span>');
            }
            submenu.prepend('<span class="menu-click"><i class="menu-arrow fa fa-angle-right"></i></span>');
            $('.menu-mobile').on('click', function() {
                $('.menu-list').slideToggle('slow');
            });
            $('.menu-click').on('click', function() {
                $(this).siblings('.sub-menu').slideToggle('slow');
                $(this).children('.menu-arrow').toggleClass('menu-extend');
            });
            $('.close, .overlapblackbg').on('click', function() {
                $(items).removeClass('menuopen').addClass('menuclose');
                $('#mobile-menu').removeClass("move-menu");
                $('.blog-main').removeClass("move-body");
            });
        },

        initializ: function() {
            responsive_menu.menu();
        }
    };

    responsive_menu.menu();
    /**
     *  Toggle Search Input
     *  -----------------------------------------------------------------------
     *  For Search button click in header
     */
    var SearchForm = '.search-form',
        BtnSearch = '.btn-form',
        ToggleSearchForm = 'toggle-search-form';

    $(BtnSearch).click(function() {
        $(SearchForm).toggleClass(ToggleSearchForm);
    });

});