import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { HighScoreService } from './highScore.service';
import { Player } from './player';

@Component({
    selector: 'high-scores',
    moduleId: module.id,
    templateUrl: './high-scores.component.html',
    providers: [HighScoreService]
})
export class HighScoresComponent implements OnInit{
    highScores: Player[];
    errorMessage: string;
    
    constructor(private highScoreService: HighScoreService) { }
    
    ngOnInit() {
        this.getHighScores();
    }
    
    getHighScores() {
        this.highScoreService.getHighScores()
            .subscribe(
                highScores => this.highScores = highScores,
                error => this.errorMessage = <any>error
            );
    }
}