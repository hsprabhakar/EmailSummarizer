export default function Table() {
  return (
        <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table className="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead className="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" className="px-6 py-3">
                            Email ID
                        </th>
                        <th scope="col" className="px-6 py-3">
                            From
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Subject
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Date
                        </th>
                        <th scope="col" className="px-6 py-3">
                            Body
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr className="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                        <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1
                        </th>
                        <td className="px-6 py-4">
                            Amazon Inc
                        </td>
                        <td className="px-6 py-4">
                            Your package has arrived
                        </td>
                        <td className="px-6 py-4">
                            Nov 21, 2024
                        </td>
                        <td className="px-6 py-4">
                            Hello ___, your amazon package has arrived ...
                        </td>
                    </tr>
                    <tr className="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1
                        </th>
                        <td className="px-6 py-4">
                            Amazon Inc
                        </td>
                        <td className="px-6 py-4">
                            Your package has arrived
                        </td>
                        <td className="px-6 py-4">
                            Nov 21, 2024
                        </td>
                        <td className="px-6 py-4">
                            Hello ___, your amazon package has arrived ...
                        </td>
                    </tr>
                    <tr className="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1
                        </th>
                        <td className="px-6 py-4">
                            Amazon Inc
                        </td>
                        <td className="px-6 py-4">
                            Your package has arrived
                        </td>
                        <td className="px-6 py-4">
                            Nov 21, 2024
                        </td>
                        <td className="px-6 py-4">
                            Hello ___, your amazon package has arrived ...
                        </td>
                    </tr>
                    <tr className="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1
                        </th>
                        <td className="px-6 py-4">
                            Amazon Inc
                        </td>
                        <td className="px-6 py-4">
                            Your package has arrived
                        </td>
                        <td className="px-6 py-4">
                            Nov 21, 2024
                        </td>
                        <td className="px-6 py-4">
                            Hello ___, your amazon package has arrived ...
                        </td>
                    </tr>
                    <tr>
                    <th scope="row" className="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            1
                        </th>
                        <td className="px-6 py-4">
                            Amazon Inc
                        </td>
                        <td className="px-6 py-4">
                            Your package has arrived
                        </td>
                        <td className="px-6 py-4">
                            Nov 21, 2024
                        </td>
                        <td className="px-6 py-4">
                            Hello ___, your amazon package has arrived ...
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    );
}