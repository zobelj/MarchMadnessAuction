<script>
    let answer = '';
    let question = '';

    async function submitQuestion() {

        console.log(question)
        // send a GET request to the api with the question
        const response = await fetch(`/api/question/${question}`);
        const json = await response.json();

        // set the answer to the response from the api
        answer = json.answer;


    }

</script>

<h1>Welcome! We have been waiting.</h1>
<h3>We know you have questions about the Auction, and we'd love to hear them.</h3>


<!-- Text box to enter a question -->

<!-- Button to submit question -->

<div>
    <input type="text" placeholder="Enter your question here" bind:value={question} />
    <button on:click={submitQuestion}>Submit</button>
</div>

<div>
    Q: {question}
</div>
<br>
<div>
    A: {answer}
</div>


<style>

    input {
        width: 80%;
        height: 50px;
        font-size: 1.5rem;
        padding: 1rem;
        border: 1px solid #ccc;
        border-radius: 0.25rem 0 0 0.25rem;
    }


</style>
