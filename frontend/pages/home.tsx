import "../app/globals.css"
import Table from "@/components/ui/table"
import SummarizeButton from "@/components/SummarizeButton"
export default function Home() {
  return (
    <>
      <div className="mx-8 my-8 py-8">      
        <div className="">
            <h1 className="text-3xl">Welcome Home</h1>
        </div>
        <div className="flex my-8 justify-center">
          <SummarizeButton /> {/*Button to summarize 10 latest emails*/}
        </div>
        <div>
            <Table />
        </div>
      </div>
    </>
  )
}