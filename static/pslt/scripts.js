$(document).ready(function () {
    /*region Listeners*/
    $(window).resize(function () {
        updateUI();
    });
    $("div.nav-bar button.menu")
        .click(function () {
            $("div.nav-menu").slideToggle({progress: updateUI});
            $(this).removeClass("active");
        });
    $("div.nav-menu button.plus-minus").click(function () {
        $(this).text(function (_, value) {
            return value === '+' ? '-' : '+'
        });
        $(this).parent().next().slideToggle({progress: updateUI});
    });
    $("div.desktop-nav-bar li.desktop-top-nav-link").hover(
        function () {
            $(this).find("ul.desktop-nav-hidden").css("display", "table");
        },
        function () {
            $(this).find("ul.desktop-nav-hidden").css("display", "none");
        }
    );
    /*endregion*/

    /*region Init UI*/
    $("div.nav-menu dd").hide();
    updateUI();
    /*endregion*/
});

function updateUI() {
    /*region Footer*/
    var epsilon = 10;
    var footer = $("div.footer");
    footer.css("margin-top", epsilon);
    if ($("body").innerHeight() > window.innerHeight + epsilon) {
        // if there's more than a page of content, position the footer normally
        footer.css("position", "inherit");
        footer.css("bottom", "auto");
    } else {
        // otherwise, have it float to the bottom
        footer.css("position", "absolute");
        footer.css("bottom", "0");
    }
    /*endregion*/

    /*region Team Page*/
    var team_member_images = $("div.team-member img");
    try {
        var team_member_image_width = team_member_images[0].width;
        team_member_images.css("height", team_member_image_width)
    } catch (ex) {

    }
    /*endregion*/

    /*region Outreach Page*/
    $("div.outreach-img-wrapper").each(function (index) {
        var img = $(this).find("img");
        var canvas = $(this).find("canvas.gradient");
        var fab = $(this).find("a.outreach-fab");

        var newLeft = (img[0].width / 2) - (fab.outerWidth() / 2);
        fab.css("left", newLeft);

        canvas.css("height", img[0].height);
        canvas.css("width", img[0].width);

        var ctx = canvas[0].getContext("2d");
        var grd = ctx.createLinearGradient(0, 0, 0, canvas[0].height);
        grd.addColorStop(0, "transparent");
        grd.addColorStop(0.4, "transparent");
        grd.addColorStop(1, "black");
        ctx.fillStyle = grd;
        ctx.clearRect(0, 0, canvas[0].width, canvas[0].height);
        ctx.fillRect(0, 0, canvas[0].width, canvas[0].height);
    })
    /*endregion*/
}