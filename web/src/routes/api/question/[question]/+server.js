export const GET = async ({ params }) => {
    const question = params.question;

    console.log('GET', question);
    let res = await fetch(`http://127.0.0.1:5174/run_prompt/${question}`, {
        method: 'GET',
        mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json'
        },

    });

    return res;

};

