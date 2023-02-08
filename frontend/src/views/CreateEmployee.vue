<script setup lang="ts">

</script>

<template>
    <div>
        <h5 class="text-lg font-semibold text-center">Create Employee</h5>

        <div class="flex justify-center border p-3 mt-3 rounded-md">
            <div>
                <form>
                    <input type="text" class="input w-96 mb-3" required placeholder="Firstname *"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Lastname *"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Lastname *"/> <br/>
                    <input type="text" class="input w-96 mb-3" required placeholder="Department *"/> <br/>
                    <input type="number" class="input w-96 mb-3" required placeholder="Salary per hour *"/> <br/>
                    <input type="number" class="input w-96 mb-3" required placeholder="Hours per week *"/>
                    
                    <div class="mb-3">
                        <label class="font-semibold">Birthday *</label>
                        <div class="relative max-w-sm">
                            <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                            <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path></svg>
                            </div>
                            <input datepicker type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full pl-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Select date">
                        </div>
                    </div>
                    
                    <label class="block mb-2 text-md font-medium text-white dark:text-white" for="file_input">Image</label>
                    <input class="block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="file_input" type="file">

                    <button class="bg-green-500 p-3 rounded-md w-full mt-3"><font-awesome-icon icon="fa-solid fa-plus" /> Add</button>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
.input {
    border: 2px solid #e8e8e8;
    padding: 15px;
    border-radius: 10px;
    background-color: #212121;
    font-size: small;
    font-weight: bold;
    text-align: center;
}

.input:focus {
    outline-color: white;
    background-color: #212121;
    color: #e8e8e8;
    box-shadow: 5px 5px #888888;
}
</style>