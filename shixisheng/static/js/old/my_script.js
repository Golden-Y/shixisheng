jQuery(function(e) {
    e("#carousel").elastislide({imageW: 110,margin: 20,border: 4,easing: "easeInBack"})
});
jQuery(function(e) {
    e("#ticker").tweet({username: "icanbeCreative",page: 1,avatar_size: 32,count: 20,loading_text: "loading ..."}).bind("loaded", function() {
        var t = e(this).find(".tweet_list");
        var n = function() {
            setTimeout(function() {
                t.find("li:first").animate({marginTop: "-4em"}, 500, function() {
                    e(this).detach().appendTo(t).removeAttr("style")
                });
                n()
            }, 15e3)
        };
        n()
    })
});
jQuery(document).ready(function() {
    jQuery(function() {
    })
});
$(function() {
    $("#sti-menu").iconmenu()
});
$(document).ready(function() {
    $(".img-thumb").on("mouseover", function() {
        var e = $(this).find(".overlay-wrp");
        var t = $(this).find(".overlay-content");
        var n = parseInt(e.height() * .5 - 4);
        e.stop(true, true).fadeIn(300);
        t.stop().animate({top: n}, 400)
    }).on("mouseleave", function() {
        var e = $(this).find(".overlay-wrp");
        var t = $(this).find(".overlay-content");
        var n = parseInt(e.height() * .2);
        t.stop().animate({top: n}, 100);
        e.fadeOut(200)
    })
});
$(function() {
    var e = $("#ib-main-wrapper"), t = function() {
        var t = false, n = -1, r = false, i = e.find("div.ib-main > a"), s = i.not(".ib-content"), o = s.length, u = function() {
            s.addClass("ib-image");
            a();
            l()
        }, a = function() {
            f();
            e.kinetic({moved: function() {
                    t = true
                },stopped: function() {
                    t = false
                }})
        }, f = function() {
            var t = $("#ib-top").outerHeight(true) + $("#header").outerHeight(true) + parseFloat(i.css("margin-top"));
            e.css("height", $(window).height() - t)
        }, l = function() {
            i.bind("click.ibTemplate", function(e) {
                if (!t)
                    c($(this));
                return false
            });
            $(window).bind("resize.ibTemplate", function(e) {
                f();
                $("#ib-img-preview, #ib-content-preview").css({width: $(window).width(),height: $(window).height()})
            })
        }, c = function(e) {
            if (r)
                return false;
            if (e.hasClass("ib-content")) {
                r = true;
                n = e.index(".ib-content");
                p(e, function() {
                    r = false
                })
            } else {
                r = true;
                n = e.index(".ib-image");
                h(e, function() {
                    r = false
                })
            }
        }, h = function(t, n) {
            var r = t.children("img").data("largesrc"), i = t.children("span").text(), s = {src: r,description: i};
            t.addClass("ib-loading");
            d(r, function() {
                t.removeClass("ib-loading");
                var u = $("#ib-img-preview").length > 0;
                if (!u)
                    $("#previewTmpl").tmpl(s).insertAfter(e);
                else
                    $("#ib-img-preview").children("img.ib-preview-img").attr("src", r).end().find("span.ib-preview-descr").text(i);
                var a = w(r);
                t.removeClass("ib-img-loading");
                $("#ib-img-preview").css({width: t.width(),height: t.height(),left: t.offset().left,top: t.offset().top}).children("img.ib-preview-img").hide().css({width: a.width,height: a.height,left: a.left,top: a.top}).fadeIn(400).end().show().animate({width: $(window).width(),left: 0}, 500, "easeOutExpo", function() {
                    $(this).animate({height: $(window).height(),top: 0}, 400, function() {
                        var e = $(this);
                        e.find("span.ib-preview-descr, span.ib-close").show();
                        if (o > 1)
                            e.find("div.ib-nav").show();
                        if (n)
                            n.call()
                    })
                });
                if (!u)
                    v()
            })
        }, p = function(t, n) {
            var r = $("#ib-content-preview").length > 0, i = t.children("div.ib-teaser").html(), s = t.children("div.ib-content-full").html(), o = {teaser: i,content: s};
            if (!r)
                $("#contentTmpl").tmpl(o).insertAfter(e);
            $("#ib-content-preview").css({width: t.width(),height: t.height(),left: t.offset().left,top: t.offset().top}).show().animate({width: $(window).width(),left: 0}, 500, "easeOutExpo", function() {
                $(this).animate({height: $(window).height(),top: 0}, 400, function() {
                    var e = $(this), t = e.find("div.ib-teaser"), o = e.find("div.ib-content-full"), u = e.find("span.ib-close");
                    if (r) {
                        t.html(i);
                        o.html(s)
                    }
                    t.show();
                    o.show();
                    u.show();
                    if (n)
                        n.call()
                })
            });
            if (!r)
                m()
        }, d = function(e, t) {
            $("<img/>").load(function() {
                if (t)
                    t.call()
            }).attr("src", e)
        }, v = function() {
            var e = $("#ib-img-preview");
            e.find("span.ib-nav-prev").bind("click.ibTemplate", function(e) {
                g("prev")
            }).end().find("span.ib-nav-next").bind("click.ibTemplate", function(e) {
                g("next")
            }).end().find("span.ib-close").bind("click.ibTemplate", function(e) {
                y()
            });
            $(window).bind("resize.ibTemplate", function(t) {
                var n = e.children("img.ib-preview-img"), r = w(n.attr("src"));
                n.css({width: r.width,height: r.height,left: r.left,top: r.top})
            })
        }, m = function() {
            $("#ib-content-preview").find("span.ib-close").bind("click.ibTemplate", function(e) {
                b()
            })
        }, g = function(t) {
            if (r)
                return false;
            r = true;
            var i = $("#ib-img-preview"), u = i.find("div.ib-loading-large");
            u.show();
            if (t === "next") {
                n === o - 1 ? n = 0 : ++n
            } else if (t === "prev") {
                n === 0 ? n = o - 1 : --n
            }
            var a = s.eq(n), f = a.children("img").data("largesrc"), l = a.children("span").text();
            d(f, function() {
                u.hide();
                var t = w(f);
                i.children("img.ib-preview-img").attr("src", f).css({width: t.width,height: t.height,left: t.left,top: t.top}).end().find("span.ib-preview-descr").text(l);
                e.scrollTop(a.offset().top).scrollLeft(a.offset().left);
                r = false
            })
        }, y = function() {
            if (r)
                return false;
            r = true;
            var e = s.eq(n);
            $("#ib-img-preview").find("span.ib-preview-descr, div.ib-nav, span.ib-close").hide().end().animate({height: e.height(),top: e.offset().top}, 500, "easeOutExpo", function() {
                $(this).animate({width: e.width(),left: e.offset().left}, 400, function() {
                    $(this).fadeOut(function() {
                        r = false
                    })
                })
            })
        }, b = function() {
            if (r)
                return false;
            r = true;
            var e = i.not(".ib-image").eq(n);
            $("#ib-content-preview").find("div.ib-teaser, div.ib-content-full, span.ib-close").hide().end().animate({height: e.height(),top: e.offset().top}, 500, "easeOutExpo", function() {
                $(this).animate({width: e.width(),left: e.offset().left}, 400, function() {
                    $(this).fadeOut(function() {
                        r = false
                    })
                })
            })
        }, w = function(e) {
            var t = new Image;
            t.src = e;
            var n = $(window).width(), r = $(window).height(), i = r / n, s = t.width, o = t.height, u = o / s, a, f, l, c;
            if (i > u) {
                f = r;
                a = r / u
            } else {
                f = n * u;
                a = n
            }
            return {width: a,height: f,left: (n - a) / 2,top: (r - f) / 2}
        };
        return {init: u}
    }();
    t.init()
});
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() != 0) {
            $("#toTop").fadeIn()
        } else {
            $("#toTop").fadeOut()
        }
    });
    $("#toTop").click(function() {
        $("body,html").animate({scrollTop: 0}, 2e3)
    })
});
$(document).ready(function() {
    $("[rel=tooltip]").tooltip()
});

$(document).ready(function() {
    var e = {Android: function() {
            return navigator.userAgent.match(/Android/i)
        },BlackBerry: function() {
            return navigator.userAgent.match(/BlackBerry/i)
        },iOS: function() {
            return navigator.userAgent.match(/iPhone|iPad|iPod/i)
        },Opera: function() {
            return navigator.userAgent.match(/Opera Mini/i)
        },Windows: function() {
            return navigator.userAgent.match(/IEMobile/i)
        },any: function() {
            return e.Android() || e.BlackBerry() || e.iOS() || e.Opera() || e.Windows()
        }};
    var t = e.any();

});
$(document).ready(function() {
    $("#registerHere input").hover(function() {
        $(this).popover("show")
    });
   
});
$(document).ready(function() {
    $(".nav a").click(function() {
        $("html, body").animate({scrollTop: $($(this).attr("href")).offset().top + "px"}, {duration: 1500,easing: "easeInOutQuint"});
        return false
    })
})
