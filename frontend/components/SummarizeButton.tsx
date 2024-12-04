export default function SummarizeButton() {
    const handleSummarizeEmails = async () => {
        try {
            const response = await fetch("http://localhost:8000/api/summarize/topTenNow", {
                method: "GET",
                credentials: "include"
            });

            if (response.ok) {
                const {messages} = await response.json();
                alert(messages.split("<br>").join("\n"));
            } else {
                throw new Error("Failed to get response from backend");
            }
            
        } catch (error) {
            console.error("Failed to get response from backend", error);
        }
    }

    return (
        <button onClick={handleSummarizeEmails} className="bg-neutral-800 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded">
            Summarize my emails
        </button>
    );
}