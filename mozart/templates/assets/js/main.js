/**
* Template Name: EstateAgency - v4.6.0
* Template URL: https://bootstrapmade.com/real-estate-agency-bootstrap-template/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Toggle .navbar-reduce
   */
  let selectHNavbar = select('.navbar-default')
  if (selectHNavbar) {
    onscroll(document, () => {
      if (window.scrollY > 100) {
        selectHNavbar.classList.add('navbar-reduce')
        selectHNavbar.classList.remove('navbar-trans')
      } else {
        selectHNavbar.classList.remove('navbar-reduce')
        selectHNavbar.classList.add('navbar-trans')
      }
    })
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Search window open/close
   */
  let body = select('body');
  on('click', '.navbar-toggle-box', function(e) {
    e.preventDefault()
    body.classList.add('box-collapse-open')
    body.classList.remove('box-collapse-closed')
  })

  on('click', '.close-box-collapse', function(e) {
    e.preventDefault()
    body.classList.remove('box-collapse-open')
    body.classList.add('box-collapse-closed')
  })

  /**
   * Intro Carousel
   */
  new Swiper('.intro-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 2000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Property carousel
   */
  new Swiper('#property-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.propery-carousel-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * News carousel
   */
  new Swiper('#news-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.news-carousel-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });

  /**
   * Testimonial carousel
   */
  new Swiper('#testimonial-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.testimonial-carousel-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Property Single carousel
   */
  new Swiper('#property-single-carousel', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.property-single-carousel-pagination',
      type: 'bullets',
      clickable: true
    }
  });


  

jQuery(document).ready(function($) {
  if( $('.multiple-file-upload').length > 0 ) {
    var itemTemplate = $('#mfu-item-template');
    var itemsContainer = $('#mfu-items-container');
    var itemNumber = 1;
    
    createMfuItem(itemTemplate, itemsContainer, itemNumber);
    itemNumber++;
    
    $('#mfu-new-item-btn').click(function(e) {
      createMfuItem(itemTemplate, itemsContainer, itemNumber);
      itemNumber++;
    });
  }
});

function createMfuItem(itemTemplate, itemsContainer, itemNumber) {
  itemTemplateHtml = itemTemplate.html().replace(/\{ITEM_NUMBER\}/g, itemNumber);
  itemsContainer.append( itemTemplateHtml );
}


$("body").on('click', '.mfuDeleteBtn', function(e) {
  console.log($(e.target).attr('data-send'));
  $.ajax({
    method: "POST",
    url: $(e.target).attr('data-url'),
    data: $(e.target).attr('data-send')
  })
  .done(function( msg ) {
    $(e.target).closest('.forDelete').find('.server-response').html(msg).show();
    var activitySelectWrap = $(e.target).closest(".forDelete");
    activitySelectWrap.remove();
  })
  .fail(function() {
    $(e.target).closest('.forDelete').find('.server-response').html('Ошибка удаления').show();
  });
});

})()


const aboutContainers = document.querySelectorAll('.about-container');

// Attach a click event listener to each "about-container"
aboutContainers.forEach(container => {
  const header = container.querySelector('.about-header');
  const content = container.querySelector('.about-content');
  const title = container.querySelector('.about-title');

  // Function to toggle the visibility of the content when the header is clicked
  function toggleContent() {
    content.style.display = content.style.display === 'none' ? 'block' : 'none';
    title.textContent = content.style.display === 'none' ? '+ Example Headline' : '- Example Headline';
  }

  // Add event listener to the header
  header.addEventListener('click', toggleContent);
});

