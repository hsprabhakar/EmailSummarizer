export default function SummarizeButton() {
    const handleSummarizeEmails = async () => {
        const numberOfEmails = 10;
        try {
            const response = await fetch(`http://localhost:8000/api/summarize/top_emails?number=${numberOfEmails}`, {
                method: "GET",
                credentials: "include",
            });

            if (response.ok) {
                const { messages } = await response.json();

                // Format the messages into a readable string
                const formattedMessages = messages
                    .map(
                        (message) =>
                            `Subject: ${message.subject}\nSender: ${message.sender}\nSnippet: ${message.snippet}\n`
                    )
                    .join("\n--------------------\n");

                alert(formattedMessages);
            } else {
                throw new Error("Failed to get response from backend");
            }
        } catch (error) {
            console.error("Failed to get response from backend", error);
            alert("An error occurred while fetching email summaries.");
        }
    };

    return (
        <button
            onClick={handleSummarizeEmails}
            className="bg-neutral-800 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded"
        >
            Summarize my emails
        </button>
    );
}
