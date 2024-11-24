import { Label } from "@/components/ui/label"
import "../app/globals.css"
import Table from "@/components/ui/table"
export default function Home() {
  return (
    <>
        <div className="flex justify-center my-8 ...">
            <Label className="text-3xl">Welcome Home</Label>
        </div>
        <div className="mx-8 my-8 ...">
            <Table />
        </div>
    </>
  )
}