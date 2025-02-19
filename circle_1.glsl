uniform vec2 pos;
uniform vec3 color;


void mainImage(out vec4 fragColor, in vec2 fragCoord) {

    // Normalized pixel coordinates (from 0 to 1)
    vec2 uv = fragCoord/iResolution.xy;
    vec2 npos = pos/iResolution.xy;

    // Position of fragment relative to center of screen
    vec2 rpos = npos - uv;
    // Adjust y by aspect ratio
    rpos.y /= iResolution.x/iResolution.y;


    // How far is the current pixel from the origin (0, 0)

    float distance = length(rpos);

    // Use an inverse 1/distance to set the fade

    float scale = 0.02;
    float fade = 1.5;
    float strength = 1.0 / distance * scale;



    // Fade our white color

    vec3 color = strength * color;

    color = 1.0 - exp( -color);


    // Output to the screen
    fragColor = vec4(color, 1.0);
}