window.onresize = function () {
    general_set_width();
}

function general_set_width() {
    const window_w = document.documentElement.clientWidth;
    const general_element = document.getElementById("general");
    if (window_w <= 1600) {
        general_element.style.width = "100%";
    } else {
        general_element.style.width = 1200 + 'px';
    }
}

function header_click() {
    const window_h = document.documentElement.clientHeight;
    const window_w = document.documentElement.clientWidth;
    alert(window_w + '-' + window_h);
}

function mystart() {
    general_set_width();
}

$(function () {
    // 网页上下滚动事件
    // $(window).scroll(function () {
    //     const regionTop = $(window).scrollTop();
    //     if (regionTop <= $('#general').height()) {
    //         if (regionTop >= 38) {
    //             $('#region1').offset({top: regionTop});
    //         } else {
    //             $('#region1').offset({top: 38});
    //         }
    //         if (regionTop >= 278) {
    //             $('#region2').offset({top: regionTop});
    //         } else {
    //             $('#region2').offset({top: 278});
    //         }
    //         if (regionTop >= 678) {
    //             $('#region3').offset({top: regionTop});
    //         } else {
    //             $('#region3').offset({top: 678});
    //         }
    //     }
    // })
})
