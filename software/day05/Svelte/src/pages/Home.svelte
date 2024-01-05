<script>
    import { Button, Heading } from 'flowbite-svelte';
    import { navigate } from "svelte-routing";

    const goToLogin = () => {
        navigate("/login");
    }

    const goToRegister = () => {
        navigate("/register");
    }
</script>

<div class="flex flex-col text-center">
    <Heading id="app-title" tag="h1" class="text-center">Artists Book</Heading>
    <br/>
    <p id="app-sub-title" class="text-lg text-center">Manage your favorite Artists</p>
    <br/>
</div>
<div class="text-center">
    <Button id="homePage-login-button" on:click={goToLogin}>Login</Button>
    <Button id="homePage-register-button" on:click={goToRegister}>Create an account</Button>
</div>
