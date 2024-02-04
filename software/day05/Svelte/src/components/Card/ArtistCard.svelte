<script lang="ts">
    import { Card, Avatar, Rating } from "flowbite-svelte";
    import type { Artist } from "../../types/Artist.svelte";

    export let artist:Artist;
</script>

<Card>
    <div class="flex justify-between items-center">
        <Avatar size="lg" src={artist.photoUrl} />
        <div class="text-center">
            <p class="font-semibold text-lg">{artist.name}</p>
            <p>{artist.nationality}</p>
        </div>
        <div class="text-center">
            <Rating total={5} rating={artist.rating} />
            <p>{artist.musicGender}</p>
        </div>
    </div>
</Card>