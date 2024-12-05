import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableFooter,
    TableHead,
    TableHeader,
    TableRow,
} from "@/components/ui/table"

interface Email {
    subject: string;
    sender: string;
    snippet: string
}

interface EmailTableProps {
    emails: Email[];
}

export default function EmailTable({ emails }: EmailTableProps) {
    return (
        <Table>
            <TableCaption>A list of your recent emails.</TableCaption>
            <TableHeader>
                <TableRow>
                    <TableHead className="w-[100px]">Sender</TableHead>
                    <TableHead>Subject</TableHead>
                    <TableHead>Snippet</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {emails.map((email, index) => (
                    <TableRow key={index}>
                        <TableCell>{email.sender}</TableCell>
                        <TableCell>{email.subject}</TableCell>
                        <TableCell>{email.snippet}</TableCell>
                    </TableRow>
                ))}
            </TableBody>
        </Table>
    )
}