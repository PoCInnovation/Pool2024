<script>
    import { Button, Heading, Input } from "flowbite-svelte";
    import { navigate } from "svelte-routing";

    let email = "";
    let password = "";

    const userLoggedIn = () => {
        console.log("Email", email);
        console.log("Password", password);
        navigate("/dashboard");
    }

    const goToRegister = () => {
        navigate("/register");
    }
</script>

<Heading id="app-title" tag="h1" class="text-center">Login</Heading>
<br/>
<br/>
<div class="flex flex-col items-center">
    <Input type="email" placeholder="Email" bind:value={email} class="w-96 m-1 mt-2"/>
    <Input type="password" placeholder="Password" bind:value={password} class="w-96 m-1 "/>
</div>
<br/>
<div class="text-center">
    <Button id="loginPage-login-button" on:click={userLoggedIn}>Login</Button>
    <Button id="loginPage-register-button" on:click={goToRegister}>New user ? Register</Button>
</div>
<br/>
