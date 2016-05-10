import { Component } from '@angular/core';
import { HighScoresComponent } from './high-scores.component';

@Component({
    selector: 'scorecast',
    template: `
        <h1>Scorecast</h1>
        <high-scores></high-scores>
    `,
    directives: [HighScoresComponent]
})
export class ScorecastComponent {}