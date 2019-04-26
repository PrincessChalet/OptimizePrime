var coreCount = 1;

function toggleCourseInfo(event, el) {

    console.log(el);

    $(el).toggleClass("courseNameHighlight");
    $("[id='"+event+"']").toggle();
    $("[id='"+event+"']").css("padding-left","2em");
}


$(document).ready(function(){
    $("#coreButton").bind("click", function(e){
        coreCount += 1;
        console.log(coreCount);
        e.preventDefault();

        var $newDiv = $("<div>", {id:coreCount});
        $("#uniCore").append($newDiv);

        var newBreak = "<br>";
        var newPrompt = "<b>Enter the name of the University Core section: </b>";
        var newInput = "<input type='text' name='sectionName' placeholder='Ex. Communications'>";
        var newHourPrompt = "<b>Enter the number of credits for the section: </b>";
        var newHourInput = "<input type='text' name='sectionHours' placeholder='Ex. 5'>";
        var $newRemoveButton = $("<button>", {
            class: "remover",
            text: "Remove Section"
        });

        $("#"+coreCount).append(newBreak, newPrompt, newInput, newBreak, newBreak, newHourPrompt, newHourInput, $newRemoveButton);
    });

    $(".remover").on("click",function(e){
        e.preventDefault();
        console.log("Removing");
    });

    $(".loading").click(function(){
        $('<h2>Loading</h2>').prependTo(document.body);
    });
});

$(document).on("click", ".remover", function(e){
    e.preventDefault();
    console.log("removing");

    $(this).parent().remove()
});

$(".loading").click( function(){
    console.log("trying to load");
    $('<div>Loading</div>').prependTo(document.body);
});

function removeCoreSection(event) {
    console.log(event);    
}

function tst() {
    console.log("working")
}