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
<Input type="email" placeholder="Email" bind:value={email} />
<Input type="password" placeholder="Password" bind:value={password} />
<br/>
<Button id="loginPage-login-button" on:click={userLoggedIn}>Login</Button>
<Button id="loginPage-register-button" on:click={goToRegister}>New user ? Register</Button>
