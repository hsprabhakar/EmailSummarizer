import {
    Accordion,
    AccordionContent,
    AccordionItem,
    AccordionTrigger,
} from "@/components/ui/accordion"
import "../app/globals.css"


export function DetailsAccordion() { 
    return (
        <Accordion type="single" collapsible className="w-full">
            <AccordionItem value="item-1">
                <AccordionTrigger>4,000+ unread and counting?</AccordionTrigger>
                <AccordionContent>
                Ignore them all and read just one a day.
                </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-2">
                <AccordionTrigger>Don't want to create yet another account for your task management purposes?</AccordionTrigger>
                <AccordionContent>
                Email Summarizer sends it right to your inbox.
                </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-3">
                <AccordionTrigger>Can I customize what to summarize?</AccordionTrigger>
                <AccordionContent>
                Set the topics YOU want to focus on, and we'll take care of the rest.
                </AccordionContent>
            </AccordionItem>
            </Accordion>
        )
}