% Sellmeier Coefficients for SCHOTT K7 Glass
B1 = 1.1273555;
B2 = 0.124412303;
B3 = 0.827100531;

C1 = 0.00720341707; % um^2
C2 = 0.0269835916;  % um^2
C3 = 100.384588;    % um^2

% Function handle for refractive index n(lambda in um)
n_sellmeier = @(lambda) sqrt(1 + ...
    (B1 .* lambda.^2) ./ (lambda.^2 - C1) + ...
    (B2 .* lambda.^2) ./ (lambda.^2 - C2) + ...
    (B3 .* lambda.^2) ./ (lambda.^2 - C3));

% 1. Refractive Index at Fraunhofer D line (587.56 nm = 0.58756 um)
lambda_D = 0.58756; 
nD = n_sellmeier(lambda_D);

% 2. Calculate Abbe Number (V_d = (n_d - 1) / (n_F - n_C))
lambda_F = 0.48613; % Fraunhofer F line (486.13 nm)
lambda_C = 0.65627; % Fraunhofer C line (656.27 nm)

nF = n_sellmeier(lambda_F)
nC = n_sellmeier(lambda_C)
Vd = (nD - 1) / (nF - nC);

% Display results in console
fprintf('Refractive index at Fraunhofer D-line (587.6 nm): n_D = %.5f\n', nD);
fprintf('Abbe number for SCHOTT K7: V_d = %.2f\n', Vd);

% 3. Plotting n(lambda) over the transparent spectrum (0.35 um to 2.5 um)
lambda_range = linspace(0.35, 2.5, 1000); % um
n_range = n_sellmeier(lambda_range);

figure('Color', 'w');
plot(lambda_range, n_range, 'b-', 'LineWidth', 2);
hold on;
plot(lambda_D, nD, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');

grid on;
title('Refractive Index of SCHOTT K7 Crown Glass');
xlabel('Wavelength \lambda (\mum)');
ylabel('Refractive Index n(\lambda)');
legend('Sellmeier dispersion n(\lambda)', sprintf('n_D = %.5f at 587.6 nm', nD), 'Location', 'northeast');

% Print / Save the plot to an image file
print('-dpng', '-r300', 'SCHOTT_K7_Refractive_Index.png');