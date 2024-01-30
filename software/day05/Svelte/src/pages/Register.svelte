<script>
    import { Button, Heading, Input } from "flowbite-svelte";
    import { navigate } from "svelte-routing";

    let email = "";
    let password = "";
    let confirmedPassword = "";

    const userRegistered = () => {
        console.log("Email", email);
        console.log("Password", password);
        console.log("Confirmed password", confirmedPassword);
        navigate("/dashboard");
    }

    const goToLogin = () => {
        navigate("/login");
    }
</script>

<Heading tag="h1" class="text-center">Register</Heading>
<br/>
<div class="flex flex-col items-center">
    <Input type="email" placeholder="Email" bind:value={email} class="w-96 m-1 mt-3"/>
    <Input type="password" placeholder="Password" bind:value={password} class="w-96 m-1"/>
    <Input type="password" placeholder="Confirm password" bind:value={confirmedPassword} class="w-96 m-1"/>
</div>
<br/>
<div class="flex justify-center">
    <Button id="registerPage-register-button" on:click={userRegistered} class="mr-2">Register</Button>
    <Button id="registerPage-login-button" on:click={goToLogin}>Already a user ? Login</Button>
</div>
