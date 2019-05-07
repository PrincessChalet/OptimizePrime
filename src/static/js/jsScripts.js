var coreCount = 1;
var courseCount = 1;
var sectionCount =1;
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

});
$(document).ready(function(){
    $("#courseButton").bind("click", function(e){
        courseCount += 1;
        console.log(courseCount);
        e.preventDefault();

        var $newDiv = $("<div>", {id:courseCount});
        $("#degreeRequirement").append($newDiv);

        var newBreak = "<br>";
        var newPrompt = "<b>Enter the name of the course: </b>";
        var newInput = "<input type='text' name='courseName' placeholder='Ex. CSCE 1030'>";
        var $newRemoveButton = $("<button>", {
            class: "remover",
            text: "Remove Section"
        });

        $("#"+courseCount).append(newBreak, newPrompt, newInput, newBreak, newBreak);
    });

});
$(document).ready(function(){
    $("#newSectionButton").bind("click", function(e){
        sectionCount += 1;
        console.log(sectionCount);
        e.preventDefault();

        var secID = "dR" + String(sectionCount)
        var $newDiv = $("<div>", {id:secID});
        $("#degreeRequirement").append($newDiv);


        var newBreak = "<br>";
        var newHeader = "<h2>Degree Requirements</h2>";
        var electiveInput = "<input type='radio' value='elective'>Elective<br></br>";
        var majReqInput = "<input type='radio' value='degree requirement'> Major Requirement<br></br>";
        var degreeRequirementSection = "<div>Enter the Degree Requirement Section: <input type='text' name='degreeRequirements'></div>";
        var numCredits = "<b>Enter the number of credits for the section: </b><input type='text' name='degreeSectionHours' placeholder='Ex. 5'></input>";
        var newPrompt = "<b>Enter the name of the course: </b>";
        var newInput = "<input type='text' name='courseName' placeholder='Ex. CSCE 1030'>";
        var course = "<button class='addingCourse'> Add Another Course </button>";
 

        $("#"+secID).append(newBreak, newHeader, electiveInput, majReqInput, degreeRequirementSection, numCredits, newBreak, newPrompt, course, newInput, newBreak, newBreak);
    });

});
$(document).on("click", ".remover", function(e){
    e.preventDefault();
    console.log("removing");

    $(this).parent().remove()
});

$(document).on("click", ".addingCourse", function(e) {
    e.preventDefault();
    console.log("adding course");

    var newInput = "<input type='text' name='courseName' placeholder='Ex. CSCE 1030'>";
    $(this).parent().append(newInput)
})

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

function addCore(){
    console.log("unicore");
    
}