function toggleCourseInfo(event, el) {

    console.log(el);

    $(el).toggleClass("courseNameHighlight");
    $("[id='"+event+"']").toggle();
    $("[id='"+event+"']").css("padding-left","2em");
}